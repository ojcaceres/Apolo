import os, django, glob, sys, shelve

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Apolo.settings")

import django
import openpyxl

django.setup()

from apps.autenticacion.models import USUARIO
from django.contrib.auth.models import Group
from apps.estructura.models import Modulo, Estado
from django.db.models import Q

#USUARIO.objects.filter(~Q(username='admin')).delete()
wb = openpyxl.load_workbook('USUARIOS-APOLO-ESTACIONES 19_02_2021.xlsx')
worksheet = wb.worksheets[0]

excel_data = list()
for row in worksheet.iter_rows():
    row_data = list()
    for cell in row:
        row_data.append(str(cell.value))
    excel_data.append(row_data)


def get_stados_by_name(name):
    estados = [x.upper() for x in name.split(";") if x is not None]

    listado = []
    for x in estados:
        print(x)
        if x == "NONE":
            continue
        listado.append(
            Estado.objects.get(nombre=x.strip())
        )

    return listado


for i, linea in enumerate(excel_data):
    if i == 0:
        continue

    try:
        estados = get_stados_by_name(linea[6])

        usuario = USUARIO.objects.create(
            first_name=linea[1],
            email=linea[4] + "@noexist.com",
            last_name="",
            username=linea[4],
        )
        usuario.estado.add(*estados)
        usuario.set_password(linea[3])
        usuario.save()
    except Exception as e:
        print(linea)
        print(str(e))
