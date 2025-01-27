# Django
from django.contrib.auth import authenticate

# Rest-Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed

# Project
from apps.user.models import User


class UserSignInSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    username = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'password']

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials.')

        token, created = Token.objects.get_or_create(user=user)

        return {
            'user': user,
            'token': token.key
        }
