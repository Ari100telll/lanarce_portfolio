from django.urls import path

from lanarce_portfolio.images.api.views import ImagesCreateListAPI, ImageUpdateDeleteAPI
from lanarce_portfolio.portfolios.api.views import PortfoliosCreateListAPI, PortfoliosUpdateDeleteAPI

app_name = "images"

urlpatterns = [
    path(
        "", ImagesCreateListAPI.as_view(), name="images-create-list"
    ),
    path(
        "<uuid:image_id>/", ImageUpdateDeleteAPI.as_view(), name="image-update-delete"
    ),
]
