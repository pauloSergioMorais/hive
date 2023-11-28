from django.apps import AppConfig
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model
import os


class FilmeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filme'

    def ready(self):
        User = get_user_model()
        email = os.getenv("EMAIL_ADMIN")
        senha = os.getenv("SENHA_ADMIN")

        try:
            usuario = User.objects.get(email=email)
        except ObjectDoesNotExist:
            User.objects.create_superuser(username="admin", email=email, password=senha, is_active=True, is_staff=True)