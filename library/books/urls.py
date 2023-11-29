from rest_framework import routers
from django.urls import path, include

from .endpoints import BookViewSet, AuthorViewSet


router = routers.SimpleRouter()
router.register("bookviewset", BookViewSet)
router.register("authorviewset", AuthorViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
