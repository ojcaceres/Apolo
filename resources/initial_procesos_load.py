import os, django, glob, sys, shelve

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Apolo.settings")
django.setup()

import openpyxl
from apps.estructura.models import Estado, Dependencia, Proyecto, TipologiaEspecifica
from apps.contratacion.models import Proceso, UsuariosProcesos
from apps.autenticacion.models import USUARIO

Proceso.objects.all().delete()

wb = openpyxl.load_workbook('BASE DE DATOS MODERNIZACION RRHH 2021 ver3-26022021 apolo.xlsx')
worksheet = wb.worksheets[0]

excel_data = list()
for row in worksheet.iter_rows():
    row_data = list()
    for cell in row:
        valor = '' if cell.value is None else str(cell.value)
        row_data.append(valor)
    excel_data.append(row_data)

list_procesos = []
for i, row in enumerate(excel_data):
    if i < 2:
        continue

    try:
        estado = Estado.objects.get(nombre=row[18].upper())
        dependencia, created = Dependencia.objects.get_or_create(nombre=row[4])

        if Proyecto.objects.filter(numero=row[3]).exists():
            proyecto = Proyecto.objects.get(numero=row[3])
        else:
            proyecto = Proyecto.objects.create(numero=row[3], nombre=str(row[3]))

        tipologia = TipologiaEspecifica.objects.filter(nombre=row[7]).first()

        proc = Proceso(
            nombre_contratista=row[1],
            cedula_contratista=row[2],
            proyecto=proyecto,
            dependencia_contratista=dependencia,
            caso_seven=row[6],
            numero_de_proceso=row[7],
            vigencia=row[9],
            objeto=row[10],
            numero_cdp=row[11],
            numero_crp=row[12],
            valor_contrato=row[14],
            plazo=row[17],
            estado=estado,
            tipologia_especifica_id=tipologia.pk if tipologia else None
        )
        proc.save()

        usuario = USUARIO.objects.get(username=row[19])
        UsuariosProcesos(
            proceso=proc,
            usuario=usuario,
            estado=estado
        ).save()
        # proc.usuarios.add(usuario)
        # proc.save()

    except Exception as e:
        print(row)
        print(e)
        print("\n")
