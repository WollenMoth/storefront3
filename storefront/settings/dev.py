import socket

from .common import *  # noqa: F401, F403
from .common import INTERNAL_IPS, MIDDLEWARE, env

DEBUG = True

SECRET_KEY = env("DJANGO_SECRET_KEY")

MIDDLEWARE += ("silk.middleware.SilkyMiddleware",)

CELERY_BROKER_URL = "redis://redis:6379/0"

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/0",
        "TIMEOUT": 10 * 60,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

EMAIL_HOST = "smtp4dev"
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_PORT = 2525

hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS += [ip[: ip.rfind(".")] + ".1" for ip in ips]

MEDIA_URL = "/media/"
