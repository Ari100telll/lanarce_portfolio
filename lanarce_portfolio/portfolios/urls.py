from django.urls import path

from lanarce_portfolio.portfolios.api.views import PortfoliosCreateListAPI, PortfoliosUpdateDeleteAPI

app_name = "portfolios"

urlpatterns = [
    path(
        "", PortfoliosCreateListAPI.as_view(), name="portfolio-create-list "
    ),
    path(
        "<uuid:portfolio_id>/", PortfoliosUpdateDeleteAPI.as_view(), name="portfolio-update-delete"
    ),
]
