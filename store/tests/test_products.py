from decimal import Decimal
import pytest
from model_bakery import baker
from rest_framework import status
from store.models import Collection, Product


@pytest.fixture
def create_product(api_client):
    def do_create_product(product):
        return api_client.post('/store/products/', product)
    return do_create_product


@pytest.fixture
def retrieve_product(api_client):
    def do_retrieve_product(product_id):
        return api_client.get(f'/store/products/{product_id}/')
    return do_retrieve_product


@pytest.mark.django_db
class TestCreateProduct:
    def test_if_user_is_anonymous_returns_401(self, create_product):
        response = create_product({'title': 'test'})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self, authenticate, create_product):
        authenticate()

        response = create_product({'title': 'test'})

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid_returns_400(self, authenticate, create_product):
        authenticate(is_staff=True)

        response = create_product({'title': ''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None

    def test_if_data_is_valid_returns_201(self, authenticate, create_product):
        authenticate(is_staff=True)
        collection = baker.make(Collection)

        response = create_product({
            'title': 'test',
            'description': 'test',
            'slug': 'test',
            'inventory': 1,
            'unit_price': Decimal(1),
            'collection': collection.id
        })

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0


@pytest.mark.django_db
class TestRetrieveProduct:
    def test_if_product_exists_returns_200(self, retrieve_product):
        product = baker.make(Product)

        response = retrieve_product(product.id)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id': product.id,
            'title': product.title,
            'collection': product.collection.id,
            'description': product.description,
            'images': [],
            'inventory': product.inventory,
            'slug': product.slug,
            'unit_price': product.unit_price,
            'price_with_tax': product.unit_price * Decimal(1.1)
        }

    def test_if_product_does_not_exist_returns_404(self, retrieve_product):
        response = retrieve_product(1)

        assert response.status_code == status.HTTP_404_NOT_FOUND
