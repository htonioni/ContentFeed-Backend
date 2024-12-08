from rest_framework import serializers
from django.core import exceptions
import django.contrib.auth.password_validation as validators
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from users.models import User
from rest_framework.exceptions import AuthenticationFailed

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        validated_data = super().validate(data)
        user = User.objects.filter(email=validated_data['email']).first()
        self.user = authenticate(
            username=user.username,
            password=validated_data["password"],
        )
        if not self.user:
            raise AuthenticationFailed(
                detail="Unable to login with provided credentials."
            )
        return validated_data

    def create(self, validated_data):
        return Token.objects.get_or_create(user=self.user)[0]

