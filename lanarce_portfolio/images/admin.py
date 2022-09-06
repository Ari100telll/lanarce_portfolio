from django.contrib import admin

from lanarce_portfolio.images.models import Image, Comment


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


class CommentsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_by",
        "text",
        "rate",
        "image",
        "created_at",
    )
    list_filter = ("image", "created_by")


admin.site.register(Image, ImageAdmin)
admin.site.register(Comment, CommentsAdmin)
