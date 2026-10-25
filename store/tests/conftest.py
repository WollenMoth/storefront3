import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def authenticate(api_client):
    def do_authenticate(is_staff=False):
        api_client.force_authenticate(user=get_user_model()(is_staff=is_staff))

    return do_authenticate
