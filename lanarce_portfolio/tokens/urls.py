from django.urls import path

from lanarce_portfolio.tokens.api.views import DynamicLifetimeTokenObtainPairView

app_name="tokens"

urlpatterns = [
    path(
        "", DynamicLifetimeTokenObtainPairView.as_view(), name="token-obtain-pair"
    ),
]
