from django.urls import path

from lanarce_portfolio.feed.api.views import ImageFeedListAPI
from lanarce_portfolio.images.api.views import ImagesCreateListAPI, ImageUpdateDeleteAPI
from lanarce_portfolio.portfolios.api.views import PortfoliosCreateListAPI, PortfoliosUpdateDeleteAPI

app_name = "feed"

urlpatterns = [
    path(
        "", ImageFeedListAPI.as_view(), name="images-feed-list"
    ),
]
