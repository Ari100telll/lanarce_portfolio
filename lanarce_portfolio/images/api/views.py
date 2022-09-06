from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.views import APIView

from lanarce_portfolio.images.api.serializers import ImageSerializer, ImageInputSerializer
from lanarce_portfolio.images.selectors import get_portfolio_images, get_user_image_by_id
from lanarce_portfolio.images.services import create_image, update_image, delete_image
from lanarce_portfolio.portfolios.models import Portfolio
from lanarce_portfolio.utils.exception_handler import ApiErrorsMixin


class ImagesCreateListAPI(ApiErrorsMixin, ListAPIView):
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        portfolio_id = self.kwargs.get("portfolio_id")
        return get_portfolio_images(portfolio=portfolio_id)

    def post(self, request, portfolio_id, *args, **kwargs):
        serializer = ImageInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        portfolio = get_object_or_404(Portfolio, id=portfolio_id)
        create_image(portfolio=portfolio, **serializer.validated_data)

        return Response(status=HTTP_201_CREATED)


class ImageUpdateDeleteAPI(ApiErrorsMixin, APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, image_id, *args, **kwargs):
        serializer = ImageInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        image = get_user_image_by_id(image_id=image_id, user=self.request.user)

        update_image(image=image, **serializer.validated_data)

        return Response(status=HTTP_204_NO_CONTENT)

    def delete(self, request, image_id, *args, **kwargs):
        image = get_user_image_by_id(image_id=image_id, user=self.request.user)

        delete_image(image=image)

        return Response(status=HTTP_204_NO_CONTENT)
