from rest_framework import serializers

from lanarce_portfolio.images.models import Image
from lanarce_portfolio.portfolios.api.serializers import PortfolioSerializer


class ImageSerializer(serializers.ModelSerializer):
    portfolio = PortfolioSerializer()
    file = serializers.SerializerMethodField()

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
