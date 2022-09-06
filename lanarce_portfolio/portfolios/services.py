from django.contrib.auth import get_user_model

from lanarce_portfolio.portfolios.models import Portfolio
from lanarce_portfolio.utils.common import model_update

User = get_user_model()


def create_portfolio(
        *,
        owner: User,
        name: str,
        description: str,
) -> Portfolio:
    portfolio = Portfolio.objects.create(
        owner=owner,
        name=name,
        description=description,
    )
    return portfolio


def update_portfolio(
        *,
        portfolio: Portfolio,
        **portfolio_details,
) -> Portfolio:
    updated_portfolio, _ = model_update(
        instance=portfolio,
        fields=list(portfolio_details.keys()),
        data=portfolio_details
    )

    return updated_portfolio


def delete_portfolio(
        *,
        portfolio: Portfolio,
) -> None:
    portfolio.delete()
