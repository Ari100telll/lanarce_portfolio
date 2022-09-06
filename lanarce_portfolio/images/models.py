from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import CASCADE, ForeignKey, TextField, IntegerField, DateTimeField, CharField, DecimalField, \
    ImageField

from lanarce_portfolio.portfolios.models import Portfolio
from lanarce_portfolio.utils.base_models import BaseUUIDModel

# Create your models here.

User = get_user_model()


def get_file_upload_path(instance, filename):
    return f"{instance.portfolio.owner.username}/{instance.portfolio.name}/images/{filename}"


class Image(BaseUUIDModel):
    name = CharField(
        max_length=120,
        blank=False,
        null=False,
        unique=True,
    )
    description = TextField(blank=True, null=True)
    portfolio = ForeignKey(
        Portfolio,
        null=False,
        blank=False,
        on_delete=CASCADE,
        related_name="images",
        help_text="The portfolio to which the images belong"
    )
    file = ImageField(
        upload_to=get_file_upload_path,
        null=False,
        blank=False,
    )

    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(BaseUUIDModel):
    created_by = ForeignKey(
        User,
        null=False,
        blank=False,
        on_delete=CASCADE,
        related_name="creator",
        help_text="Comment creator"
    )

    text = TextField(null=False, blank=False, help_text="Comment text")
    rate = IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], null=True)
    image = ForeignKey(
        Image,
        null=False,
        blank=False,
        on_delete=CASCADE,
        related_name="image",
        help_text="Image"
    )

    created_at = DateTimeField(auto_now_add=True)
