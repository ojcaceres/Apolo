import os, django, glob, sys, shelve

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Apolo.settings")

import django

django.setup()
from apps.contratacion.models import Proceso, ProcesoEstados
from apps.estructura.models import Proyecto, Estado, Modulo

estado = Estado.objects.filter(nombre="SECOP_PUBLICACION").first()
procestado = ProcesoEstados.__getitem__("SECOP_PUBLICACION")
print(procestado)