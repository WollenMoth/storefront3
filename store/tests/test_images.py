from io import BytesIO

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from model_bakery import baker
from PIL import Image
from rest_framework import status

from store.models import Product, ProductImage


@pytest.mark.django_db
@pytest.mark.parametrize("image_format", ["PNG", "JPEG", "WEBP"])
def test_upload_image_round_trip(
    api_client, authenticate, settings, tmp_path, image_format
):
    settings.MEDIA_ROOT = tmp_path
    authenticate(is_staff=True)
    product = baker.make(Product)
    data = BytesIO()
    Image.new("RGB", (24, 16), color="blue").save(data, format=image_format)
    upload = SimpleUploadedFile(
        f"product.{image_format.lower()}",
        data.getvalue(),
        content_type=f"image/{image_format.lower()}",
    )

    response = api_client.post(
        f"/store/products/{product.pk}/images/", {"image": upload}, format="multipart"
    )

    assert response.status_code == status.HTTP_201_CREATED
    saved = ProductImage.objects.get(pk=response.data["id"])
    assert saved.product_id == product.pk
    with saved.image.open("rb") as file, Image.open(file) as image:
        image.load()
        assert image.size == (24, 16)
        assert image.format == image_format


@pytest.mark.django_db
def test_rejects_invalid_image(api_client, settings, tmp_path):
    settings.MEDIA_ROOT = tmp_path
    product = baker.make(Product)
    upload = SimpleUploadedFile("fake.jpg", b"not an image", content_type="image/jpeg")

    response = api_client.post(
        f"/store/products/{product.pk}/images/", {"image": upload}, format="multipart"
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "image" in response.data
    assert not ProductImage.objects.exists()


@pytest.mark.django_db
def test_rejects_oversized_image(api_client, settings, tmp_path):
    settings.MEDIA_ROOT = tmp_path
    product = baker.make(Product)
    data = BytesIO()
    Image.new("RGB", (24, 16)).save(data, format="PNG")
    upload = SimpleUploadedFile(
        "large.png", data.getvalue() + b"x" * (501 * 1024), content_type="image/png"
    )

    response = api_client.post(
        f"/store/products/{product.pk}/images/", {"image": upload}, format="multipart"
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "500 KB" in str(response.data["image"])
    assert not ProductImage.objects.exists()
