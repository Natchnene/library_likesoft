from rest_framework import routers
from django.urls import path, include

from .endpoints import UserCreateAPIView


urlpatterns = [
    path("register/", UserCreateAPIView.as_view(), name="register"),
]
