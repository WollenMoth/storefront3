"""Isolated test settings; never use the developer's database or external services."""

import os

# common.py reads .env, so override the database before importing it.
os.environ["DATABASE_URL"] = os.environ.get("TEST_DATABASE_URL", "sqlite:///:memory:")

from .common import *  # noqa: E402, F403
from .common import env  # noqa: E402

DEBUG = False
SECRET_KEY = "storefront-tests-only-not-a-production-secret-key"
ALLOWED_HOSTS = ["testserver", "localhost", "127.0.0.1"]
DATABASES = {"default": env.dj_db_url("DATABASE_URL")}
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
CACHES = {"default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"}}
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True
LOGGING = {"version": 1, "disable_existing_loggers": False}
