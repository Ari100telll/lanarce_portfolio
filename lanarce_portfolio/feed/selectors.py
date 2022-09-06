from django.contrib.auth import get_user_model

from lanarce_portfolio.images.models import Image, Comment

User = get_user_model()


def get_all_images(user: User):
    return Image.objects.exclude(portfolio__owner=user)


def get_all_image_comments(image: Image):
    return Comment.objects.filter(image=image)
