from django.urls import path

from lanarce_portfolio.users.api.views import UserCreateRetrieveUpdateDeleteAPI

app_name = "users"

urlpatterns = [
    path(
        "", UserCreateRetrieveUpdateDeleteAPI.as_view(), name="token-obtain-pair"
    ),
]
