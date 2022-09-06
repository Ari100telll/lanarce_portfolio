from django.urls import path

from lanarce_portfolio.feed.api.views import ImageFeedListAPI, ImageCommentsListCreateAPI
from lanarce_portfolio.images.api.views import ImagesCreateListAPI, ImageUpdateDeleteAPI
from lanarce_portfolio.portfolios.api.views import PortfoliosCreateListAPI, PortfoliosUpdateDeleteAPI

app_name = "feed"

urlpatterns = [
    path(
        "", ImageFeedListAPI.as_view(), name="images-feed-list"
    ),
    path(
        "<uuid:image_id>/", ImageCommentsListCreateAPI.as_view(), name="images-comments-list-create"
    ),
]
