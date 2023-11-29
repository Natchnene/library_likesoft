from rest_framework import routers
from django.urls import path, include

from .endpoints import BookViewSet


router = routers.SimpleRouter()
router.register("bookviewset", BookViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
