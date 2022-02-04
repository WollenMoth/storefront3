from djoser.serializers import (
    UserSerializer as BaseUserSerializer,
    UserCreateSerializer as BaseUserCreateSerializer,
)
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as BaseTokenObtainPairSerializer


class UserCreateSerializer(BaseUserCreateSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    def get_token(self, user):
        refresh = RefreshToken.for_user(user)

        addClaims(refresh, user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password',
                  'email', 'first_name', 'last_name', 'token']


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class TokenObtainPairSerializer(BaseTokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        addClaims(token, user)

        return token


def addClaims(token, user):
    token['username'] = user.username
    token['email'] = user.email
    token['is_staff'] = user.is_staff
    return token
