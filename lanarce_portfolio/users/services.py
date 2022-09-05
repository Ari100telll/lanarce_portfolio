from django.contrib.auth import get_user_model
from django.db import transaction

User = get_user_model()


def create_user(
        *,
        username: str,
        email: str,
        phone_number: str,
        password: str,
        position: str
) -> User:
    user = User.objects.create_user(
        username=username,
        email=email,
        phone_number=phone_number,
        is_active=True,
        password=password,
        position=position,
    )
    return user
