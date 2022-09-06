from django.urls import path

from lanarce_portfolio.users.api.views import UserCreateRetrieveUpdateDeleteAPI

app_name = "users"

urlpatterns = [
    path(
        "", UserCreateRetrieveUpdateDeleteAPI.as_view(), name="users-retrieve-update-delete"
    ),
    path(
        "change_password", UserCreateRetrieveUpdateDeleteAPI.as_view(), name="users-retrieve-update-delete"
    ),
]
