from django.apps import AppConfig
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model
import os


class FilmeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filme'
    
    # def ready(self):