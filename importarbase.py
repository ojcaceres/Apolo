import os, django, glob, sys, shelve

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Apolo.settings")

import django

django.setup()
from apps.contratacion.models import Proceso, ProcesoEstados, Modificacion, ModificacionesProcesos
from apps.contratacion.views.views_genericos import asignar
from apps.autenticacion.models import USUARIO
from apps.estructura.models import Estado
from datetime import datetime



f = open("resources/suspension.csv", "r")
for i, line in enumerate(f):
    line = line.split('|')
    no_contrato = line[0]
    vigencia = line[1]
    modificacion = "SUSPENSION"
    print(no_contrato)
    try:
        historialprocesos = Proceso.objects.filter(numero_contrato=no_contrato, vigencia="2021")
        print("adicionando modificacion")
        mod = "SU"

        try:
            fecha_firma_modificacion = datetime.strptime(line[16],  "%d/%m/%Y")
        except Exception as e:
            fecha_firma_modificacion = None
            print(f'line {i} error: {e}')
        try:
            fechaInicio = datetime.strptime(line[13],  "%d/%m/%Y")
        except Exception as e:
            fechaInicio = None
            print(f'line {i} error: {e}')
        try:
            fechaFin = datetime.strptime(line[14],  "%d/%m/%Y")
        except Exception as e:
            fechaFin = None
            print(f'line {i} error: {e}')
        try:
            fechaReinicio = datetime.strptime(line[14],  "%d/%m/%Y")
        except Exception as e:
            fechaReinicio = None
            print(f'line {i} error: {e}')

        estado = Estado.objects.filter(nombre=line[17]).first()
        usuario = USUARIO.objects.filter(username=line[15]).filter(is_active=True).first()
        modifica = Modificacion.objects.create(
            modificacion=modificacion,
            numero_contrato=no_contrato,
            vigencia=vigencia,
        )

        proc = Proceso.objects.create(
            numero_de_proceso=mod + "-" + no_contrato + "-" + vigencia,
            modificacion=modificacion,
            nombre_contratista=historialprocesos.last().nombre_contratista,
            cedula_contratista=historialprocesos.last().cedula_contratista,
            numero_contrato=no_contrato,
            vigencia=vigencia,
            link=historialprocesos.last().link,
            dependencia_contratista=historialprocesos.last().dependencia_contratista,
            fecha_radicacion=fecha_firma_modificacion,
            proyecto=historialprocesos.last().proyecto,
            tipologia_especifica=historialprocesos.last().tipologia_especifica,
            objeto=historialprocesos.last().objeto,
            usuario=usuario,
            estado=estado,
            nombre_supervisor=historialprocesos.last().nombre_supervisor,
            fecha_inicio=fechaInicio,
            fecha_final=fechaFin)

        procestado = ProcesoEstados.__getitem__(line[17])
        asignar(proc.id, procestado , "Cargado automaticamente por Apolo", usuario.id)
        ModificacionesProcesos.objects.create(modificacion=modifica, proceso=proc)
    except Exception as e:
        fecha_firma_modificacion = None
        print(f'line {i} error: {e}')

g = open("resources/adiciones.csv", "r")
for i, line in enumerate(g):
    line = line.split('|')
    no_contrato = line[0]
    vigencia = line[1]
    modificacion = "ADICION_PRORROGA"
    print(no_contrato)
    try:
        historialprocesos = Proceso.objects.filter(numero_contrato=no_contrato, vigencia="2021")
        print("adicionando modificacion")
        mod = "AP"

        try:
            fecha_firma_modificacion = datetime.strptime(line[12],  "%d/%m/%Y")
        except Exception as e:
            fecha_firma_modificacion = None
            print(f'line {i} error: {e}')
        try:
            fechaInicio = datetime.strptime(line[15],  "%d/%m/%Y")
        except Exception as e:
            fechaInicio = None
            print(f'line {i} error: {e}')
        try:
            fechaFin = datetime.strptime(line[16],  "%d/%m/%Y")
        except Exception as e:
            fechaFin = None
            print(f'line {i} error: {e}')
        try:
            fechaReinicio = datetime.strptime(line[16],  "%d/%m/%Y")
        except Exception as e:
            fechaReinicio = None
            print(f'line {i} error: {e}')

        estado = Estado.objects.filter(nombre=line[11]).first()
        usuario = USUARIO.objects.filter(username=line[10]).filter(is_active=True).first()
        modifica = Modificacion.objects.create(
            modificacion=modificacion,
            numero_contrato=no_contrato,
            vigencia=vigencia,
            fechaInicio=fechaInicio,
            fechaFin = fechaFin,
            fechaReinicio = fechaReinicio,
            cdp = line[13],
            valor = line[14]
        )

        proc = Proceso.objects.create(
            numero_de_proceso=mod + "-" + no_contrato + "-" + vigencia,
            modificacion=modificacion,
            nombre_contratista=historialprocesos.last().nombre_contratista,
            cedula_contratista=historialprocesos.last().cedula_contratista,
            numero_contrato=no_contrato,
            vigencia=vigencia,
            link=historialprocesos.last().link,
            dependencia_contratista=historialprocesos.last().dependencia_contratista,
            fecha_radicacion=fecha_firma_modificacion,
            proyecto=historialprocesos.last().proyecto,
            tipologia_especifica=historialprocesos.last().tipologia_especifica,
            objeto=historialprocesos.last().objeto,
            usuario=usuario,
            estado=estado,
            nombre_supervisor=historialprocesos.last().nombre_supervisor,
            fecha_inicio=fechaInicio,
            fecha_final=fechaFin)

        procestado = ProcesoEstados.__getitem__(line[11])
        asignar(proc.id, procestado , "Cargado automaticamente por Apolo", usuario.id)
        ModificacionesProcesos.objects.create(modificacion=modifica, proceso=proc)
    except Exception as e:
        fecha_firma_modificacion = None
        print(f'line {i} error: {e}')
