from django.contrib.auth import get_user_model
from django.db.models import CASCADE, CharField, TextField, ForeignKey, DateTimeField

from lanarce_portfolio.utils.base_models import BaseUUIDModel

User = get_user_model()


class Portfolio(BaseUUIDModel):
    name = CharField(
        max_length=120,
        blank=False,
        null=False,
        unique=True,
    )
    description = TextField(help_text="portfolios description")
    owner = ForeignKey(
        User,
        null=False,
        blank=False,
        on_delete=CASCADE,
        related_name="portfolios",
        help_text="Portfolios owner"
    )

    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
