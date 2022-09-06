from django.contrib import admin

from lanarce_portfolio.images.models import Image
from lanarce_portfolio.portfolios.models import Portfolio


class ImageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
        "portfolio",
        "file",
        "created_at",
    )
    list_filter = ("portfolio",)


admin.site.register(Image, ImageAdmin)
