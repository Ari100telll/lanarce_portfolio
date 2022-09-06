from django.contrib.auth import get_user_model
from rest_framework import serializers

from lanarce_portfolio.portfolios.models import Portfolio

User = get_user_model()


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "position",
        )


class PortfolioSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer(many=False)

    class Meta:
        model = Portfolio
        fields = (
            "id",
            "name",
            "description",
            "owner",
            "created_at",
        )


class PortfolioInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = (
            "name",
            "description",
        )
