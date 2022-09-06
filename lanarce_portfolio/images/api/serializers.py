from django.contrib.auth import get_user_model
from rest_framework import serializers

from lanarce_portfolio.images.models import Image, Comment
from lanarce_portfolio.portfolios.api.serializers import PortfolioSerializer

User = get_user_model()


class ImageSerializer(serializers.ModelSerializer):
    portfolio = PortfolioSerializer()

    class Meta:
        model = Image
        fields = (
            "id",
            "name",
            "description",
            "portfolio",
            "file",
        )


class ImageInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            "name",
            "description",
            "file",
        )


class CommentsCreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "position",
        )


class CommentsSerializer(serializers.ModelSerializer):
    created_by = CommentsCreatorSerializer()
    image = ImageSerializer()

    class Meta:
        model = Comment
        fields = (
            "created_by",
            "text",
            "rate",
            "image",
            "created_at",
        )
