from django.core.management.base import BaseCommand
from django.db import connection
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
import datetime
from apps.autenticacion.models import USUARIO
from apps.estructura.models import Estado 
from apps.contratacion.models import Proceso, UsuariosProcesos


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        fix_procesos()
      
def fix_procesos():

    #obtener usuario y estado del proceso 

    procesos = Proceso.objects.all()

    for proceso in procesos:
        if proceso.usuario:
            if proceso.estado.nombre == "SUBSANACION":
                estado = Estado.objects.filter(nombre="REVISAR").first() 
                print("SUBSANACION")
                UsuariosProcesos.objects.create(
                        usuario=proceso.usuario,
                        proceso=proceso,
                        estado=estado
                    )
            else:
                print(proceso.usuario)
                print(proceso.estado)
                UsuariosProcesos.objects.create(
                            usuario=proceso.usuario,
                            proceso=proceso,
                            estado=proceso.estado
                        )
