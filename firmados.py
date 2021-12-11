import os
import sys
import django

import random

from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.db.models import Count, Min, Max, Avg


os.environ['DJANGO_SETTINGS_MODULE'] = 'Apolo.settings'
django.setup()

from apps.contratacion.models import Proceso, UsuariosProcesos
from apps.estructura.models import Estado
from apps.autenticacion.models import EstadosDeUsuarios


procesos = Proceso.objects.all()

for proceso in procesos:
    estado = Estado.objects.filter(nombre="FIRMADO").first()
    estado_asignado = Estado.objects.filter(nombre="SOLICITUD_CRP").first()
    if proceso.estado == estado:
        proceso.estado = estado_asignado
        proceso.save()
        

for proceso in procesos:
    estado = Estado.objects.filter(nombre="ACTIVO").first()
    estado_asignado = Estado.objects.filter(nombre="SECOP_PUBLICACION").first()
    if proceso.estado == estado:
        proceso.estado = estado_asignado
        proceso.save()



#asignar usuarios a estado
estadousers = EstadosDeUsuarios.objects.all()

for estadouser in estadousers:
    estado = Estado.objects.filter(nombre="ACTIVO").first()
    estado_asignado = Estado.objects.filter(nombre="SECOP_PUBLICACION").first()
    if estadouser.estado == estado:
        estadouser.estado = estado_asignado
        estadouser.save()
print("asignados usuarios a SECOP_PUBLICACION")
        
#asignar usuario procesos



userprocesos = UsuariosProcesos.objects.all()

for userproceso in userprocesos:
    estado = Estado.objects.filter(nombre="ACTIVO").first()
    estado_asignado = Estado.objects.filter(nombre="SECOP_PUBLICACION").first()
    if userproceso.estado == estado:
        userproceso.estado = estado_asignado
        userproceso.save()
print("asignados usuarios a Procesos  SECOP_PUBLICACION")

print("favor no ejecutar este proceso de nuevo")
