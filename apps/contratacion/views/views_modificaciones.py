from django.contrib.auth.decorators import  login_required
from django.shortcuts import render
from django.db import connection
from apps.contratacion.models import Proceso, ProcesoEstados, Modificacion, ModificacionesProcesos
from apps.contratacion.views.views_genericos import asignar
from datetime import datetime


#CREACION PROCESO DE MODIFICACION
@login_required(login_url="/login/")
def CreacionModificacion(request):
        class variables:
            duracion = ""
            fecha_firma_modificacion = ""
            fechaInicio = ""
            fechaFin = ""
            fechaReinicio = ""
            valor = ""
            documentoCedente = ""
            cedente = ""
            documentoCesionario = ""
            cesionario = ""

        resultado = None
        if request.method == "POST":
            print(request.POST)
            no_contrato = request.POST.get('contrato')
            vigencia = request.POST.get('select2')
            modificacion = request.POST.get('select3')
            boton=request.POST.get('filtrar')
            historialprocesos= Proceso.objects.filter(numero_contrato=no_contrato, vigencia=vigencia)
            if historialprocesos.count() > 0 :
                resultado=True
                variables.cdp = historialprocesos.last().numero_cdp
                variables.valor = historialprocesos.last().valor_cdp
                variables.documentoCedente = historialprocesos.last().cedula_contratista
                variables.cedente = historialprocesos.last().nombre_contratista
                variables.documentoCesionario = historialprocesos.last().cedula_contratista
                variables.cesionario = historialprocesos.last().nombre_contratista

            print(resultado)
            mod=""
            if modificacion == "OTROSI" : mod="OT"
            elif modificacion == "ADICION": mod="AD" 
            elif modificacion == "CESION": mod="CE"
            elif modificacion == "PRORROGA": mod= "PR"
            elif modificacion == "SUSPENSION": mod= "SU"
            elif modificacion == "REINICIO": mod="RE"
            elif modificacion == "ADICION_PRORROGA": mod="AP"
            elif modificacion == "ADICION_PRORROGA_OTROSI": mod="APO"
            elif modificacion == "ADICION_PRORROGA_SUSPENSION": mod="APS"
            elif modificacion == "TERMINACION_ANTICIPADA": mod= "TA"

            if boton == "Crear Modificacion" :
                    variables.duracion = request.POST.get('duracion')
                    variables.cdp = request.POST.get('cdp')
                    variables.fecha_firma_modificacion = datetime.strptime(request.POST.get('fecha_firma_modificacion'),"%Y-%m-%d")
                    variables.fechaInicio =  datetime.strptime(request.POST.get('fechaInicio'),"%Y-%m-%d")
                    variables.fechaFin =  datetime.strptime(request.POST.get('fechaFin'),"%Y-%m-%d")
                    variables.fechaReinicio  = datetime.strptime(request.POST.get('fechaReinicio'),"%Y-%m-%d")
                    variables.valor = request.POST.get('valor')
                    variables.documentoCedente = request.POST.get('documentoCedente')
                    variables.cedente = request.POST.get('cedente')
                    variables.documentoCesionario = request.POST.get('documentoCesionario')
                    variables.cesionario = request.POST.get('cesionario')

                    modifica= Modificacion.objects.create(
                        modificacion=modificacion,
                        numero_contrato=no_contrato, 
                        vigencia=vigencia,
                        duracion=variables.duracion,
                        )

                    proc= Proceso.objects.create(
                        numero_de_proceso=mod+  "-"+no_contrato+"-"+vigencia,
                        modificacion=modificacion,
                        nombre_contratista=variables.cesionario,
                        cedula_contratista=variables.documentoCesionario,
                        numero_cdp=variables.cdp,
                        numero_contrato=no_contrato, 
                        vigencia=vigencia,
                        link=historialprocesos.last().link,
                        dependencia_contratista=historialprocesos.last().dependencia_contratista,
                        fecha_radicacion=variables.fecha_firma_modificacion,
                        valor_cdp=variables.valor,
                        valor_contrato=historialprocesos.last().valor_contrato,
                        proyecto=historialprocesos.last().proyecto,
                        tipologia_especifica=historialprocesos.last().tipologia_especifica,
                        objeto=historialprocesos.last().objeto,
                        nombre_supervisor=historialprocesos.last().nombre_supervisor,
                        fecha_inicio=variables.fechaInicio,
                        fecha_final=variables.fechaFin   )

                    asignar(proc.id, ProcesoEstados.REVISIONMOD)
                    ModificacionesProcesos.objects.create(modificacion = modifica, proceso = proc)

            #Si es Busqueda
            else:
                print(historialprocesos)      

        else:
            no_contrato = ""
            historialprocesos = None

        print(historialprocesos)

        return render(request,'modificaciones/creacion.html', { 'numerocontrato': no_contrato, 'procesoraiz': historialprocesos, 'resultado': resultado , 'variables': variables })


