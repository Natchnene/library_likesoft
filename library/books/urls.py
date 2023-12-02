from rest_framework import routers
from django.urls import path, re_path, include

from .endpoints import BookViewSet, AuthorViewSet, BooksAuthorAPIView


router = routers.SimpleRouter()
router.register("bookviewset", BookViewSet)
router.register("authorviewset", AuthorViewSet)

urlpatterns = [
    path("", include(router.urls)),
    re_path("author/(?P<id>[^/.]+)", BooksAuthorAPIView.as_view(), name="author_books")
]
