from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView

app_name = "tokens"

urlpatterns = [
    path(
        "", TokenObtainPairView.as_view(), name="token-obtain-pair"
    ),
    path("refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("logout/", TokenBlacklistView.as_view(), name="logout"),

]
