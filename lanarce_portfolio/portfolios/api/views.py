from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.views import APIView

from lanarce_portfolio.portfolios.api.serializers import PortfolioSerializer, PortfolioInputSerializer
from lanarce_portfolio.portfolios.models import Portfolio
from lanarce_portfolio.portfolios.selectors import get_user_portfolios
from lanarce_portfolio.portfolios.services import create_portfolio, update_portfolio, delete_portfolio
from lanarce_portfolio.utils.exception_handler import ApiErrorsMixin


class PortfoliosCreateListAPI(ApiErrorsMixin, ListAPIView):
    serializer_class = PortfolioSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return get_user_portfolios(user=self.request.user)

    def post(self, request, *args, **kwargs):
        serializer = PortfolioInputSerializer(data=request.data)
        serializer.is_valid()

        create_portfolio(owner=self.request.user, **serializer.validated_data)

        return Response(status=HTTP_201_CREATED)


class PortfoliosUpdateDeleteAPI(ApiErrorsMixin, APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, portfolio_id, *args, **kwargs):
        serializer = PortfolioInputSerializer(data=request.data)
        serializer.is_valid()

        portfolio = get_object_or_404(Portfolio, id=portfolio_id)

        update_portfolio(portfolio=portfolio, **serializer.validated_data)

        return Response(status=HTTP_204_NO_CONTENT)

    def delete(self, request, portfolio_id, *args, **kwargs):
        portfolio = get_object_or_404(Portfolio, id=portfolio_id)

        delete_portfolio(portfolio=portfolio)

        return Response(status=HTTP_204_NO_CONTENT)
