import socket

from .common import *  # noqa: F401, F403
from .common import INSTALLED_APPS, INTERNAL_IPS, MIDDLEWARE, env

DEBUG = True

SECRET_KEY = env("DJANGO_SECRET_KEY")

INSTALLED_APPS += ["debug_toolbar", "silk"]
MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "silk.middleware.SilkyMiddleware",
]

CELERY_BROKER_URL = env("REDIS_URL", "redis://localhost:6379/0")

CACHES = {"default": env.dj_cache_url("CACHE_URL", default=CELERY_BROKER_URL)}
CACHES["default"].setdefault("TIMEOUT", env.int("CACHE_TIMEOUT", default=600))

hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS += [ip[: ip.rfind(".")] + ".1" for ip in ips]

MEDIA_URL = "/media/"
