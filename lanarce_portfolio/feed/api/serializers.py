from rest_framework import serializers

from lanarce_portfolio.images.api.serializers import CommentsCreatorSerializer, ImageSerializer
from lanarce_portfolio.images.models import Image, Comment
from lanarce_portfolio.portfolios.api.serializers import PortfolioSerializer


class ImageFeedSerializer(serializers.ModelSerializer):
    portfolio = PortfolioSerializer()

    class Meta:
        model = Image
        fields = (
            "id",
            "name",
            "description",
            "portfolio",
            "file",
            "created_at",
        )


class ImageCommentsSerializer(serializers.ModelSerializer):
    created_by = CommentsCreatorSerializer()
    image = ImageSerializer()

    class Meta:
        model = Comment
        fields = (
            "text",
            "rate",
            "image",
            "created_at",
            "created_by",
        )


class ImageCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "text",
            "rate",
        )
