from django.contrib import admin
from django import forms

from . import models


class PlanAnualAdminForm(forms.ModelForm):

    class Meta:
        model = models.PlanAnual
        fields = "__all__"


class PlanAnualAdmin(admin.ModelAdmin):
    form = PlanAnualAdminForm
    list_display = [
        "estadodelcupo",
        "nombreplan",
        "vigencia",
        "proyecto",
        "nombreproyecto",
        "fuentedefinanciacion",
        "componentegasto",
        "unidadoperativa",
        "localidad",
        "nombrerubroprespupuestal",
        "pmrcodigo",
        "pmrnombre",
        "metacodigo",
        "nombredelameta",
        "codigoactividad",
        "nombreactividad",
        "nombreservicio",
        "descripcioncupo",
        "idcupo",
        "fechaestimadaproceso",
        "fechaestimadacompra",
        "fechaestimadapago",
        "fecha_radicacion",
        "plazo",
        "presupuestoprogramado",
        "modificaciones",
        "ejecucion",
        "presupuestovigente",
        "cupoconvigenciafutura",
        "descripcionobjeto",
        "nombremodalidadadquisicion",
        "modalidaddeseleccion",
        "nombremodalidadseleccion",
        "tipodecontratacion",
        "nombretipodecontratacion",
        "individualconjunta",
        "dependencia",
        "nombredependencia",
        "numerocdp",
        "valorcdp",
        "fechadesolicituddecdp",
        "fechadecdp",
        "saldodecupodespuesdecdp",
        "objetodelcontrato",
        "valordelcrp",
        "saldodedisponibilidadesporcomprometer",
        "fechadegiros",
        "compromisossinautorizacion",
        "historicocaso",
    ]
  

class BaseAdminForm(forms.ModelForm):

    class Meta:
        model = models.Base
        fields = "__all__"


class BaseAdmin(admin.ModelAdmin):
    form = BaseAdminForm
    list_display = [
        "numero_contrato",
        "tipologia",
        "modalidad",
        "fechasuscripcion",
        "fechafinal",
        "plazo",
        "idcupo",
        "numerocdp",
        "numerocrp",
        "idcupoaju",
        "fecharegistro",
        "fuente",
        "proyecto",
        "tipoidcontratista",
        "numeroid",
        "nombrecontratista",
        "idsupervisor",
        "nombresupervisor",
        "valorcrp",
        "anulaciones",
        "valorneto",
        "valorcontrato",
    ]
    readonly_fields = [
        "numero_contrato",
        "tipologia",
        "modalidad",
        "fechasuscripcion",
        "fechafinal",
        "plazo",
        "idcupo",
        "numerocdp",
        "numerocrp",
        "idcupoaju",
        "fecharegistro",
        "fuente",
        "proyecto",
        "tipoidcontratista",
        "numeroid",
        "nombrecontratista",
        "idsupervisor",
        "nombresupervisor",
        "valorcrp",
        "anulaciones",
        "valorneto",
        "valorcontrato",
    ]


admin.site.register(models.PlanAnual, PlanAnualAdmin)
admin.site.register(models.Base, BaseAdmin)
