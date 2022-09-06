from django.contrib import admin

from lanarce_portfolio.portfolios.models import Portfolio


class PortfolioAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
        "owner",
        "created_at",
    )
    list_filter = ("owner",)

admin.site.register(Portfolio, PortfolioAdmin)
