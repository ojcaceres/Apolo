import os, django, glob, sys, shelve

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Apolo.settings")

import django

django.setup()
from apps.contratacion.models import Proceso
from apps.estructura.models import Proyecto

f = open("DICIEMBRE VII.txt", "r")
for i, line in enumerate(f):
    line = line.split('|')
    try:
        proceso = Proceso.objects.filter(numero_de_proceso=line[0]).first()
        proyecto = Proyecto.objects.filter(numero=line[3]).first()

        proceso.nombre_contratista = line[1]
        proceso.cedula_contratista = line[2]
        proceso.proyecto = proyecto
        proceso.objeto = line[4]
        proceso.plazo = line[5]
        proceso.numero_cdp = line[6]
        proceso.valor_cdp = line[7]
        proceso.valor_contrato = line[8]
        proceso.save()

    except Exception as e:
        print(f'line {i} error: {e}')
