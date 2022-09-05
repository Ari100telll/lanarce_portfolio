from django.shortcuts import render
from rest_framework_simplejwt.views import TokenViewBase

from lanarce_portfolio.tokens.api.serializers import DynamicLifetimeTokenObtainPairSerializer


# Create your views here.


class DynamicLifetimeTokenObtainPairView(TokenViewBase):
    serializer_class = DynamicLifetimeTokenObtainPairSerializer
