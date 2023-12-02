from rest_framework import generics
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer
from .tasks import send_welcome_email


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        user = serializer.save()
        send_welcome_email.delay(user.id)
        return Response(serializer.data)
