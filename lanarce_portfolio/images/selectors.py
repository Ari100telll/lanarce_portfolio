from django.contrib.auth import get_user_model
from rest_framework.generics import get_object_or_404

from lanarce_portfolio.images.models import Image
from lanarce_portfolio.portfolios.models import Portfolio

User = get_user_model()


def get_portfolio_images(portfolio: Portfolio):
    return Image.objects.filter(portfolio=portfolio)


def get_user_image_by_id(user: User, image_id: str):
    return get_object_or_404(Image, id=image_id, portfolio__owner=user)
