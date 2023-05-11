from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import PasswordField

from core.models import User


class CoreSerializer(serializers.ModelSerializer):
    password = PasswordField(required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'password']

    def create(self, validated_data: dict) -> User:
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)