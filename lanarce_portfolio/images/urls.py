from django.urls import path

from lanarce_portfolio.images.api.views import ImagesCreateListAPI, ImageUpdateDeleteAPI, CommentListAPI

app_name = "images"

urlpatterns = [
    path(
        "", ImagesCreateListAPI.as_view(), name="images-create-list"
    ),
    path(
        "<uuid:image_id>/", ImageUpdateDeleteAPI.as_view(), name="image-update-delete"
    ),
    path(
        "<uuid:image_id>/comment/", CommentListAPI.as_view(), name="comment-list"
    ),

]
