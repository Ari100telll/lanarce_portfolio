from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.views import APIView

from lanarce_portfolio.permissions.base_api_permissions import method_permission_classes
from lanarce_portfolio.users.api.serializers import UserInputSerializer, UserSerializer
from lanarce_portfolio.users.services import create_user
from lanarce_portfolio.utils.exception_handler import ApiErrorsMixin


class UserCreateRetrieveUpdateDeleteAPI(ApiErrorsMixin, APIView):
    serializer_class = UserSerializer
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = UserInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = create_user(**serializer.validated_data)

        data = self.serializer_class(user).data
        return Response(data, status=HTTP_201_CREATED)

    @method_permission_classes((IsAuthenticated, ))
    def get(self, request):
        data = self.serializer_class(request.user).data
        return Response(data=data)
