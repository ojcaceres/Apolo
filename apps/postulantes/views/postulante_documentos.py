from django.core.mail import send_mail
from django.shortcuts import render
from Apolo.settings import EMAIL_HOST_USER,  APOLOHV_URL
from apps.postulantes.models import radicacion_postulante, radicacion_cdp, parametricas, cargos_dependencias, radicacion_cdp_documentos
from apps.postulantes.views.utils import numero_to_letras
from apps.postulantes.views.postulante_views import getDocumentosFromPostulante

def certificado_no_planta(request, id_cdp):
    if 'guardar' in request.POST:
        documentos = parametricas.objects.filter(categoria='documento_proceso_cargar')
        cdp = radicacion_cdp.objects.get(id=id_cdp)
        dependencias = cargos_dependencias.objects.filter(activo=1)
        dependencia_remitente = cargos_dependencias.objects.get(id=request.POST['dependencia_solicitante'])
        dependencia_destinatario = cargos_dependencias.objects.get(id=request.POST['dependencia_destinatario'])
        p = radicacion_cdp_documentos.objects.filter(id_radicacion_cdp=int(request.POST['id_radicacion_cdp'])).first()
        valor_total_contrato_letras = numero_to_letras(cdp.valor_contrato)
        plazo_ejecucion_meses = int(cdp.valor_contrato / cdp.honorarios)
        plazo_ejecucion_dias = (cdp.valor_contrato / cdp.honorarios) - plazo_ejecucion_meses
        plazo_ejecucion_dias = plazo_ejecucion_dias * 30
        plazo_ejecucion_meses_letras = numero_to_letras(plazo_ejecucion_meses)
        plazo_ejecucion_dias_letras = numero_to_letras(plazo_ejecucion_dias)
        valor_mensual_contrato_letras = numero_to_letras(cdp.honorarios)

        if (p):
            p.id_estructura_cargos_dependencias_remitente = dependencia_remitente.id
            p.nombre_remitente =dependencia_remitente.nombre_completo
            p.cargo_remitente = dependencia_remitente.cargo
            p.dependencia_remitente = dependencia_remitente.dependencia
            p.id_estructura_cargos_destinatario = dependencia_destinatario.id
            p.nombre_destinatario = dependencia_destinatario.nombre_completo
            p.unidad_operativa = request.POST['unidad_operativa']
            p.cargo_destinatario = dependencia_destinatario.cargo
            p.dependencia_destinatario = dependencia_destinatario.dependencia
            p.objeto = request.POST['ObjetoDelContrato']             
            p.experiencia_relacionada = request.POST['experiencia_relacionada']            
            p.formacion_academica = request.POST['formacion_academica']
            p.equipo_elabora = request.POST['equipo_elabora']
            p.reviso = request.POST['reviso']
            p.aprobo = request.POST['aprobo']
            p.descripcion_necesidad = request.POST['descripcion_necesidad']
            p.alcance_objeto = request.POST['alcance_objeto']
            p.objetivo = request.POST['objetivo']
            p.meta = request.POST['meta']
            p.descripcion_rubro = request.POST['descripcion_rubro']
            p.obligaciones_especificas = request.POST['obligaciones_especificas']
            p.numero_cdp = cdp.numero_cdp
            p.numero_proyecto = cdp.codigo_proyecto
            p.valor_cdp = cdp.valor_cdp
            p.valor_afectado = cdp.valor_contrato
            p.es_regimen_comun = request.POST['es_regimen_comun']
            p.plazo_ejecucion_meses = plazo_ejecucion_meses
            p.plazo_ejecucion_meses_letras = plazo_ejecucion_meses_letras #request.POST['plazo_ejecucion_meses_letras']
            p.plazo_ejecucion_dias = plazo_ejecucion_dias
            p.plazo_ejecucion_dias_letras = plazo_ejecucion_dias_letras # request.POST['plazo_ejecucion_dias_letras']
            p.valor_total_contrato_letras = valor_total_contrato_letras #request.POST['valor_total_contrato_letras']
            p.valor_mensual_contrato_letras = valor_mensual_contrato_letras #request.POST['valor_mensual_contrato_letras']
            p.aplican_garantias = request.POST['aplican_garantias']
            p.aplica_paragrafo_suspension = request.POST['aplica_paragrafo_suspension']
            p.cargo_supervisor = request.POST['cargo_supervisor']
            p.dependencia_supervisor = request.POST['dependencia_supervisor']
            p.save()
        else:
            p = radicacion_cdp_documentos(
                id_radicacion_cdp = request.POST['id_radicacion_cdp'],
                    id_estructura_cargos_dependencias_remitente =dependencia_remitente.id,
                    unidad_operativa = request.POST['unidad_operativa'],
                    nombre_remitente =dependencia_remitente.nombre_completo, 
                    cargo_remitente = dependencia_remitente.cargo,
                    dependencia_remitente = dependencia_remitente.dependencia,
                    id_estructura_cargos_destinatario = dependencia_destinatario.id,
                    nombre_destinatario = dependencia_destinatario.nombre_completo,
                    cargo_destinatario = dependencia_destinatario.cargo,
                    dependencia_destinatario = dependencia_destinatario.dependencia,
                    objeto = request.POST['ObjetoDelContrato'],              
                    experiencia_relacionada = request.POST['experiencia_relacionada'],              
                    formacion_academica = request.POST['formacion_academica'], 
                    equipo_elabora = request.POST['equipo_elabora'],
                    reviso = request.POST['reviso'],
                    aprobo = request.POST['aprobo'],
                    descripcion_necesidad = request.POST['descripcion_necesidad'],
                    objetivo = request.POST['objetivo'],
                    meta = request.POST['meta'],
                    alcance_objeto = request.POST['alcance_objeto'],
                    descripcion_rubro = request.POST['descripcion_rubro'],
                    obligaciones_especificas = request.POST['obligaciones_especificas'],
                    numero_cdp = cdp.numero_cdp,
                    numero_proyecto = cdp.codigo_proyecto,
                    valor_cdp = cdp.valor_cdp,
                    valor_afectado = cdp.valor_contrato,
                    es_regimen_comun = request.POST['es_regimen_comun'],
                    plazo_ejecucion_meses = plazo_ejecucion_meses,

                    plazo_ejecucion_meses_letras = plazo_ejecucion_meses_letras, #request.POST['plazo_ejecucion_meses_letras']
                    plazo_ejecucion_dias = plazo_ejecucion_dias,
                    plazo_ejecucion_dias_letras = plazo_ejecucion_dias_letras, # request.POST['plazo_ejecucion_dias_letras']
                    valor_total_contrato_letras = valor_total_contrato_letras, #request.POST['valor_total_contrato_letras']
                    valor_mensual_contrato_letras = valor_mensual_contrato_letras, #request.POST['valor_mensual_contrato_letras']

                    # plazo_ejecucion_meses_letras = request.POST['plazo_ejecucion_meses_letras'],
                    # plazo_ejecucion_dias = request.POST['plazo_ejecucion_dias'],
                    # plazo_ejecucion_dias_letras = request.POST['plazo_ejecucion_dias_letras'],
                    # valor_total_contrato_letras = request.POST['valor_total_contrato_letras'],
                    # valor_mensual_contrato_letras = request.POST['valor_mensual_contrato_letras'],
                    aplican_garantias = request.POST['aplican_garantias'],
                    aplica_paragrafo_suspension = request.POST['aplica_paragrafo_suspension'],
                    cargo_supervisor = request.POST['cargo_supervisor'],
                    dependencia_supervisor = request.POST['dependencia_supervisor']
            )
            p.save()
        return render(request, 'postulante/documentos_proceso.html', {'documentos': documentos, 'cdp': cdp})
        # return render(request,'postulante/documento_noplanta_print.html',{ 'cdp':cdp, 'radicacion_cdp_documentos':p})
    documentos = parametricas.objects.filter(categoria='documento_proceso_cargar')
    cdp = radicacion_cdp.objects.get(id=id_cdp)
    dependencias = cargos_dependencias.objects.filter(activo=1)
    datos_estudios = radicacion_cdp_documentos.objects.filter(id_radicacion_cdp=id_cdp).first()
    return render(request, 'postulante/documento_noplanta.html',
                  {'documentos': documentos, 'cdp': cdp, 'dependencias': dependencias,
                   'datos_estudios': datos_estudios, })


def certificado_no_planta_print(request, id_cdp):
    cdp = radicacion_cdp.objects.get(id=id_cdp)
    p = radicacion_cdp_documentos.objects.filter(id_radicacion_cdp=id_cdp).first
    return render(request, 'postulante/documento_noplanta_print.html', {'cdp': cdp, 'radicacion_cdp_documentos': p})


def certificado_idoneidad_print(request, id_cdp):
    cdp = radicacion_cdp.objects.get(id=id_cdp)
    p = radicacion_cdp_documentos.objects.filter(id_radicacion_cdp=id_cdp).first
    postulante = radicacion_postulante.objects.get(id=cdp.id_radicacion_postulante)
    documentos = getDocumentosFromPostulante(postulante.correoelectronicopersonal)

    return render(request, 'postulante/documento_idoneidad_print.html',
                  {'cdp': cdp, 'radicacion_cdp_documentos': p, 'postulante': postulante, 'documentos': documentos})

    # return render(request,'postulante/documentos_proceso.html',{ 'documentos':documentos, 'cdp':cdp })


def estudios_previos_print(request, id_cdp):
    cdp = radicacion_cdp.objects.get(id=id_cdp)
    p = radicacion_cdp_documentos.objects.filter(id_radicacion_cdp=id_cdp).first
    postulante = radicacion_postulante.objects.get(id=cdp.id_radicacion_postulante)
    return render(request, 'postulante/documento_estudios_previos_print.html',
                  {'cdp': cdp, 'radicacion_cdp_documentos': p, 'postulante': postulante, })


def obligaciones_contratista(request, id_cdp):
    cdp = radicacion_cdp.objects.get(id=id_cdp)
    p = radicacion_cdp_documentos.objects.filter(id_radicacion_cdp=id_cdp).first
    postulante = radicacion_postulante.objects.get(id=cdp.id_radicacion_postulante)
    return render(request, 'postulante/documento_estudios_previos_obligaciones.html',
                  {'cdp': cdp, 'radicacion_cdp_documentos': p, 'postulante': postulante, })

