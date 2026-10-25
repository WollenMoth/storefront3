import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import AccessToken


@pytest.mark.django_db
def test_register_login_refresh_and_authenticated_profile():
    client = APIClient()
    password = "test-only-long-random-password-1947!"
    response = client.post(
        "/auth/users/",
        {"username": "shopper", "email": "shopper@example.com", "password": password},
    )
    assert response.status_code == 201
    assert "access" in response.data["token"]
    user = get_user_model().objects.get(username="shopper")
    assert user.check_password(password)

    response = client.post(
        "/auth/jwt/create/", {"username": user.username, "password": password}
    )
    assert response.status_code == 200
    token = AccessToken(response.data["access"])
    assert token["username"] == user.username
    assert token["email"] == user.email
    assert token["is_staff"] is False

    refresh = client.post("/auth/jwt/refresh/", {"refresh": response.data["refresh"]})
    assert refresh.status_code == 200
    client.credentials(HTTP_AUTHORIZATION=f"JWT {refresh.data['access']}")
    profile = client.get("/auth/users/me/")
    assert profile.status_code == 200
    assert profile.data["id"] == user.pk


@pytest.mark.django_db
def test_invalid_credentials_do_not_issue_tokens():
    response = APIClient().post(
        "/auth/jwt/create/", {"username": "missing", "password": "wrong-password"}
    )
    assert response.status_code == 401
    assert "access" not in response.data
