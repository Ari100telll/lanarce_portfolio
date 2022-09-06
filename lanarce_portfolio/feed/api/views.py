from tkinter.tix import IMAGE

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination

from lanarce_portfolio.feed.api.serializers import ImageFeedSerializer
from lanarce_portfolio.feed.selectors import get_all_images
from lanarce_portfolio.images.models import Image
from lanarce_portfolio.utils.exception_handler import ApiErrorsMixin


class ImageFeedPagination(LimitOffsetPagination):
    default_limit = 15


class ImageFeedListAPI(ApiErrorsMixin, ListAPIView):
    pagination_class = ImageFeedPagination
    ordering = ("created_at",)
    serializer_class = ImageFeedSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ["name", "description", "portfolio__name"]

    def get_queryset(self):
        return get_all_images(user=self.request.user)
