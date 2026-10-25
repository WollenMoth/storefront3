from .common import *  # noqa: F401, F403
from .common import env

DEBUG = False

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["andrebuy.herokuapp.com"])

CELERY_BROKER_URL = env("REDIS_URL")

CACHES = {"default": env.dj_cache_url("CACHE_URL", default=CELERY_BROKER_URL)}
CACHES["default"].setdefault("TIMEOUT", env.int("CACHE_TIMEOUT", default=600))

if not env("EMAIL_URL", default=None):
    EMAIL_HOST = env("MAILGUN_SMTP_SERVER")
    EMAIL_HOST_USER = env("MAILGUN_SMTP_LOGIN")
    EMAIL_HOST_PASSWORD = env("MAILGUN_SMTP_PASSWORD")
    EMAIL_PORT = env.int("MAILGUN_SMTP_PORT")

# AWS S3 Settings

AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")

AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")

AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")

AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

AWS_LOCATION = "static"

AWS_QUERYSTRING_AUTH = False

# Static files (CSS, JavaScript, Images)

STORAGES = {
    "default": {"BACKEND": "storages.backends.s3.S3Storage"},
    "staticfiles": {"BACKEND": "storages.backends.s3.S3StaticStorage"},
}

MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/media/"
