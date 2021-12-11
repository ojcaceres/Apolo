from rest_framework import serializers

from . import models


class ProcesoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Proceso
        fields = [
            "modificacion",
            "link",
            "id_cupo",
            "numero_de_proceso",
            "cedula_contratista",
            "fecha_radicacion",
            "plazo",
            "numero_cdp",
            "valor_cdp",
            "valor_contrato",
            "numero_contrato",
            "vigencia",
            "devuelto",
            "objeto",
            "numero_crp",
            "valor_crp",
            "nombre_supervisor",
            "ultima_actualizacion",
            "caso_seven",
            "fecha_inicio",
            "fecha_final",
        ]
