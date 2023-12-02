import os

from celery import shared_task
from django.core.mail import send_mail
from .models import User


@shared_task
def send_welcome_email(user_id):
    user = User.objects.get(id=user_id)
    subject = 'Welcome to Library!'
    message = f'Hello {user.name}, welcome to Library'
    from_email = os.environ.get("EMAIL_HOST_USER")
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)

