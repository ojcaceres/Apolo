from django.core.management.base import BaseCommand
from django.db import connection
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
import datetime
from apps.autenticacion.models import USUARIO
from apps.estructura.models import Estado



class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        upload_users()
      
def upload_users():
        file = open('resources/referentes.csv', mode='r', encoding='cp1252')
        lines = file.readlines()
        file.close()
        estado = Estado.objects.filter(nombre="SUBSANACION").first() 
        for line in lines:
            columna = line.split(';')
            q = USUARIO()
            q.set_password(columna[1])
            q.last_login = datetime.datetime.now()
            q.is_superuser = "0"
            q.username = columna[2]
            q.first_name = columna[3]
            q.email = columna[4]
            q.is_staff = "1"
            q.is_active = "1"
            q.date_joined = datetime.datetime.now()
            q.last_name = columna[5]
            try:
                q.save()
            except Exception as e:
                print(f'El usuario ya ha sido registrado: \n{e}')
