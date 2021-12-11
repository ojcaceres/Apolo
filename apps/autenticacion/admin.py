from django.contrib import admin
from django import forms
from django.contrib.auth.hashers import check_password, make_password

from .models import USUARIO, EstadosDeUsuarios


@admin.register(EstadosDeUsuarios)
class EstadosDeUsuariosAdmin(admin.ModelAdmin):
    list_display = ['estado', 'usuario']
    list_filter = ['estado', 'usuario']


class EstadosDeUsuariosInline(admin.StackedInline):
    model = EstadosDeUsuarios
    list_display = ['estado', ]
    extra = 1


@admin.register(USUARIO)
class UsuarioAdmin(admin.ModelAdmin):
    inlines = [EstadosDeUsuariosInline, ]
    search_fields = ['username', 'first_name']
    list_filter = ['dependencia', 'estado']
    list_display = [
        'username', 'get_full_name',
    ]
    readonly_fields = ['last_login', ]

    def save_model(self, request, obj, form, change):
        try:
            user_database = USUARIO.objects.get(pk=obj.pk)
        except Exception:
            user_database = None

        if user_database is None \
                or not (check_password(form.data['password'], user_database.password)
                        or user_database.password == form.data['password']):
            obj.password = make_password(obj.password)
        else:
            obj.password = user_database.password
        super().save_model(request, obj, form, change)
