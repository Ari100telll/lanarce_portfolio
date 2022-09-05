from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, TextChoices
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from lanarce_portfolio.utils.base_models import BaseUUIDModel


class User(AbstractUser, BaseUUIDModel):
    phone_number = CharField(max_length=17, blank=True, null=True)
    position = CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username


