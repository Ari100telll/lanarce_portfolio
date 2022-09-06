from django.contrib.auth import get_user_model

from lanarce_portfolio.utils.common import model_update

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


def update_user(
        user: User,
        **user_details
) -> User:
    updated_user, _ = model_update(
        instance=user,
        fields=list(user_details.keys()),
        data=user_details
    )

    return updated_user


def delete_user(user: User) -> None:
    user.delete()
