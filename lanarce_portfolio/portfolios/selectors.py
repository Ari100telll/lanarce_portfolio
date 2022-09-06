from django.contrib.auth import get_user_model
from rest_framework.generics import get_object_or_404

from lanarce_portfolio.portfolios.models import Portfolio

User = get_user_model()


def get_user_portfolios(user: User):
    return Portfolio.objects.filter(owner=user)


def get_user_portfolio_by_id(user, portfolio_id):
    return get_object_or_404(Portfolio, id=portfolio_id, owner=user)
