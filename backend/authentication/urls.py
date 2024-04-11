from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import UserView

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", UserView.as_view(actions={"post": "register"})),
    path("user/", UserView.as_view(actions={"get": "list"})),
    path("user/self/", UserView.as_view(actions={"get": "retrieve_self"})),
    path("user/<int:pk>/", UserView.as_view(actions={"get": "retrieve_basic_info_by_id"}))
]