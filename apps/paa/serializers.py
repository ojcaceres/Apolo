from rest_framework import serializers

from . import models


class PlanAnualSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PlanAnual
        fields = [
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
            "unspsc",
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

class BaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Base
        fields = [
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
