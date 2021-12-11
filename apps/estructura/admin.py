from django.contrib import admin
from import_export.admin import ExportMixin
from . import models


@admin.register(models.PlanDeDesarrollo)
class pddAdmin(ExportMixin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = [
        "nombre",
    ]


@admin.register(models.Proyecto)
class proyectoAdmin(ExportMixin, admin.ModelAdmin):
    search_fields = ['nombre', "numero"]
    list_display = [
        "numero",
        "nombre",
    ]


@admin.register(models.Modulo)
class moduloAdmin(ExportMixin, admin.ModelAdmin):
    search_fields = ['nombre', ]
    list_display = [
        "id",
        "nombre",
    ]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(models.Estado)
class estadoAdmin(ExportMixin, admin.ModelAdmin):
    search_fields = ['nombre', ]
    list_filter = ['modulo']
    list_display = [
        "id",
        "nombre",
        'modulo'
    ]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(models.Dependencia)
class dependenciaAdmin(ExportMixin, admin.ModelAdmin):
    search_fields = ['nombre', ]
    list_display = [
        "id",
        "nombre",
    ]


@admin.register(models.TipologiaEspecifica)
class tipologia_especificaAdmin(ExportMixin, admin.ModelAdmin):
    search_fields = ['nombre', ]
    list_display = [
        "id",
        "nombre",
    ]
