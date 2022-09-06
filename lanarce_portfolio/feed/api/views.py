from tkinter.tix import IMAGE

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from lanarce_portfolio.feed.api.serializers import ImageFeedSerializer, ImageCommentsSerializer, \
    ImageCommentCreateSerializer
from lanarce_portfolio.feed.selectors import get_all_images, get_all_image_comments
from lanarce_portfolio.images.models import Image
from lanarce_portfolio.images.services import create_comment
from lanarce_portfolio.utils.exception_handler import ApiErrorsMixin


class ImageFeedPagination(LimitOffsetPagination):
    default_limit = 15


class ImageFeedListAPI(ApiErrorsMixin, ListAPIView):
    pagination_class = ImageFeedPagination
    ordering = ("-created_at",)
    serializer_class = ImageFeedSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    search_fields = ["name", "description", "portfolio__name"]

    def get_queryset(self):
        return get_all_images(user=self.request.user)


class ImageCommentsListCreateAPI(ApiErrorsMixin, ListAPIView):
    serializer_class = ImageCommentsSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    ordering = ("-created_at",)

    def get_queryset(self):
        image = get_object_or_404(Image, id=self.kwargs.get("image_id"))
        return get_all_image_comments(image=image)

    def post(self, request, image_id, *args, **kwargs):
        serializer = ImageCommentCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        image = get_object_or_404(Image, id=self.kwargs.get("image_id"))

        create_comment(
            image=image,
            created_by=self.request.user,
            **serializer.validated_data,
        )
        return Response(status=HTTP_201_CREATED)
