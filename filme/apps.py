from django.apps import AppConfig
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model
import os


class FilmeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filme'
    
    def ready(self):
        from .models import Usuario

        email = os.getenv("EMAIL_ADMIN")
        senha = os.getenv("SENHA_ADMIN")

        usuarios = Usuario.objects.filter(email=email)
        if not usuarios:
            Usuario.objects.create_superuser(username="paulo.morais", email=email, password=senha, is_active=True, is_staff=True)