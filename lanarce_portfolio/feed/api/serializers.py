from rest_framework import serializers

from lanarce_portfolio.images.models import Image
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
        )
