# Rest-Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token

# Project
from apps.user.models import User


class UserSignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'name',
            'surname',
            'username',
            'password'
        ]

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username is already taken.")
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')

        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        token, created = Token.objects.get_or_create(user=user)

        return {
            'user': user,
            'token': token.key
        }
