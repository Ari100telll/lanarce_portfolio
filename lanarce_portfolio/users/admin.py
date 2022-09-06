from django.contrib.auth import admin as auth_admin, get_user_model
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from lanarce_portfolio.users.forms import UserChangeForm, UserCreationForm

User = get_user_model()


# Register your models here.

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password", "email")}),
    )
    list_display = ["username", "is_superuser"]
