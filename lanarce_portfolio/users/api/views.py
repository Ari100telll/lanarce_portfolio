from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.views import APIView

from lanarce_portfolio.permissions.base_api_permissions import method_permission_classes
from lanarce_portfolio.users.api.serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer, \
    UserChangePasswordSerializer
from lanarce_portfolio.users.services import create_user, update_user, delete_user, change_password
from lanarce_portfolio.utils.exception_handler import ApiErrorsMixin


class UserCreateRetrieveUpdateDeleteAPI(ApiErrorsMixin, APIView):
    serializer_class = UserSerializer
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = create_user(**serializer.validated_data)

        data = self.serializer_class(user).data
        return Response(data, status=HTTP_201_CREATED)

    @method_permission_classes((IsAuthenticated,))
    def get(self, request):
        data = self.serializer_class(request.user).data
        return Response(data=data)

    @method_permission_classes((IsAuthenticated,))
    def put(self, request):
        serializer = UserUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        update_user(user=self.request.user, **serializer.validated_data)

        return Response(status=HTTP_204_NO_CONTENT)

    @method_permission_classes((IsAuthenticated,))
    def delete(self, request):
        delete_user(user=self.request.user)
        return Response(status=HTTP_204_NO_CONTENT)


class UserChangePasswordAPI(ApiErrorsMixin, APIView):
    def put(self, request):
        serializer = UserChangePasswordSerializer(
            data=request.data,
            context={"user": self.request.user}
        )
        serializer.is_valid(raise_exception=True)

        change_password(
            user=self.request.user,
            new_password=serializer.validated_data.get("new_password")
        )

        return Response(status=HTTP_204_NO_CONTENT)
