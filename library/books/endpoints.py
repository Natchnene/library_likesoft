from rest_framework import permissions, viewsets, generics

from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permissions = [permissions.AllowAny]


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permissions = [permissions.AllowAny]


class BooksAuthorAPIView(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        author_id = self.kwargs["id"]
        books = Book.objects.filter(author=author_id)
        return books

