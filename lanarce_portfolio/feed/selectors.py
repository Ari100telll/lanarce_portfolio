from django.contrib.auth import get_user_model

from lanarce_portfolio.images.models import Image

User = get_user_model()


def get_all_images(user: User):
    return Image.objects.exclude(portfolio__owner=user)
