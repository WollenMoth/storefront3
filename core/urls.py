from django.urls import re_path
from rest_framework_simplejwt import views
from . import views as customViews


urlpatterns = [
    re_path(r"^jwt/create/?",
            customViews.TokenObtainPairView.as_view(), name="jwt-create"),
    re_path(r"^jwt/refresh/?", views.TokenRefreshView.as_view(),
            name="jwt-refresh"),
    re_path(r"^jwt/verify/?", views.TokenVerifyView.as_view(), name="jwt-verify"),
]
