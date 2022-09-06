from django.contrib.auth import get_user_model

from lanarce_portfolio.portfolios.models import Portfolio

User = get_user_model()


def get_user_portfolios(user: User):
    return Portfolio.objects.filter(owner=user)
