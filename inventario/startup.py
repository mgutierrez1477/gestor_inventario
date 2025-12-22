from rest_framework.authtoken.models import Token
import os
from django.contrib.auth.models import User
from django.db.utils import OperationalError


def create_superuser():
    try:
        username = os.getenv("DJANGO_SUPERUSER_USERNAME")
        email = os.getenv("DJANGO_SUPERUSER_EMAIL")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD")

        if not username or not password:
            return

        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                "email": email,
                "is_staff": True,
                "is_superuser": True,
            }
        )

        if created:
            user.set_password(password)
            user.save()

        Token.objects.get_or_create(user=user)

    except OperationalError:
        pass