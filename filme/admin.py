from django.contrib import admin
from .models import Filme, Episodio, Usuario
from django.contrib.auth.admin import UserAdmin

# Para que usuário admin apareça o campo personalizado filmes-vistos
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Histórico", {'fields': ('filmes_vistos',)}),
    )

# Register your models here.
admin.site.register(Filme)
admin.site.register(Episodio)
admin.site.register(Usuario, CustomUserAdmin)
