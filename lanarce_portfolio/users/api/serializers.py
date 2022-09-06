from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "position",
            "phone_number",
        )


class UserCreateSerializer(serializers.Serializer):
    password = serializers.CharField()
    username = serializers.CharField()
    email = serializers.CharField()
    phone_number = serializers.CharField()
    position = serializers.CharField()

    def validate(self, data):
        username = data.get("username")
        email = data.get("email")

        if User.objects.filter(username=username).exists():
            raise ValidationError("User with given username already exists")

        if User.objects.filter(email=email).exists():
            raise ValidationError("User with given Email already exists")

        return data


class UserUpdateSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.CharField()
    phone_number = serializers.CharField()
    position = serializers.CharField()

    def validate(self, data):
        username = data.get("username")
        email = data.get("email")

        if User.objects.filter(username=username).exists():
            raise ValidationError("User with given username already exists")

        if User.objects.filter(email=email).exists():
            raise ValidationError("User with given Email already exists")

        return data


class UserChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate(self, data):
        user = self.context.get("user")

        if not user.check_password(data.get("old_password")):
            raise ValidationError("Incorrect old password")

        return data
