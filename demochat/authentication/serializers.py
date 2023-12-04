from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from . models import User


class UserWithTokensSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'tokens']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {
        'bad_token': 'Token is expire or invalid'
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')
