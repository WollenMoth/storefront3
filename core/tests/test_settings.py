import os
import subprocess
import sys

import pytest


@pytest.mark.parametrize("use_urls", [True, False])
def test_production_uses_s3_without_development_apps(use_urls):
    environment = {
        "PATH": os.environ["PATH"],
        "DJANGO_SETTINGS_MODULE": "storefront.settings.prod",
        "DATABASE_URL": "sqlite:///:memory:",
        "SECRET_KEY": "test-production-configuration-only-not-a-real-secret",
        "REDIS_URL": "redis://localhost:6379/0",
        "MAILGUN_SMTP_SERVER": "smtp.example.com",
        "MAILGUN_SMTP_LOGIN": "test",
        "MAILGUN_SMTP_PASSWORD": "test-only",
        "MAILGUN_SMTP_PORT": "587",
        "AWS_ACCESS_KEY_ID": "test-only",
        "AWS_SECRET_ACCESS_KEY": "test-only",
        "AWS_STORAGE_BUCKET_NAME": "test-only",
        "DATABASE_CONN_MAX_AGE": "90",
        "ALLOWED_HOSTS": "store.example.com,admin.example.com",
        "CORS_ALLOWED_ORIGINS": "https://store.example.com",
    }
    if use_urls:
        environment.update(
            {
                "CACHE_URL": "redis://localhost:6379/1?timeout=900",
                "EMAIL_URL": "submission://mailer:p%40ss@smtp.example.com:587?timeout=10",
            }
        )
        for name in tuple(environment):
            if name.startswith("MAILGUN_"):
                del environment[name]
    code = """
import django
django.setup()
from django.conf import settings
from django.core.files.storage import storages
from storages.backends.s3 import S3Storage, S3StaticStorage
assert isinstance(storages['default'], S3Storage)
assert isinstance(storages['staticfiles'], S3StaticStorage)
assert 'debug_toolbar' not in settings.INSTALLED_APPS
assert 'silk' not in settings.INSTALLED_APPS
assert settings.CACHES['default']['BACKEND'] == 'django.core.cache.backends.redis.RedisCache'
assert settings.DATABASES['default']['CONN_MAX_AGE'] == 90
assert settings.DATABASES['default']['CONN_HEALTH_CHECKS'] is True
assert settings.ALLOWED_HOSTS == ['store.example.com', 'admin.example.com']
assert settings.CORS_ALLOWED_ORIGINS == ['https://store.example.com']
assert settings.EMAIL_HOST == 'smtp.example.com'
assert settings.EMAIL_PORT == 587
import os
if 'EMAIL_URL' in os.environ:
    assert settings.CACHES['default']['LOCATION'] == 'redis://localhost:6379/1'
    assert int(settings.CACHES['default']['TIMEOUT']) == 900
    assert settings.EMAIL_HOST_USER == 'mailer'
    assert settings.EMAIL_HOST_PASSWORD == 'p@ss'
    assert settings.EMAIL_USE_TLS is True
    assert settings.EMAIL_USE_SSL is False
    assert settings.EMAIL_TIMEOUT == 10
else:
    assert settings.CACHES['default']['LOCATION'] == 'redis://localhost:6379/0'
    assert settings.CACHES['default']['TIMEOUT'] == 600
    assert settings.EMAIL_HOST_USER == 'test'
"""
    subprocess.run([sys.executable, "-c", code], env=environment, check=True)
