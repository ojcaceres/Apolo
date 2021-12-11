
from django.shortcuts import render
from Apolo.settings import EMAIL_HOST_USER, SIDEAP_URL, SIDEAP_KEY, SIDEAP_USER, APOLOHV_URL
from apps.postulantes.models import radicacion_postulante, radicacion_cdp
from apps.contratacion.models import Proceso, ProcesoEstados
from apps.contratacion.views.views_genericos import asignar
from apps.estructura.models import Proyecto, Estado
from apps.postulantes.views.paa_services import get_cdp_from_paa
from django.db.models import Sum
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from apps.postulantes.views.utils import enviar_correo

# from django.core.mail import send_mail
# Create your views here.
tipo_documento = [
    {
        'valor': 'CC',
        'texto': 'CC'
    },
    {
        'valor': 'TI',
        'texto': 'Tarjeta de Identidad'
    },
    {
        'valor': 'CE',
        'texto': 'Cédula de Extranjeria'
    },
    {
        'valor': 'RC',
        'texto': 'Registro Civil'
    },

]

estados_postulantes = [
    {'valor':1 , 'texto': 'Documentos Solicitados'},
    {'valor':2 , 'texto': 'Documentos cargados'},
    {'valor':3 , 'texto': 'En subsanacion'},
    {'valor':4 , 'texto': 'Subsanacion a revisar'},
    {'valor':5 , 'texto': 'Aprobados'},
    {'valor':6 , 'texto': 'Desistido'},
]


def nuevo(request):
    modulos = [x.nombre for x in request.user.estado.all()]
    return render(request,'postulante/create.html', {'tipo_documento' : tipo_documento, 'modulos':modulos })

def nuevo_resultado(request):
    tipo = request.POST['tipo_documento']
    numero = request.POST['numero_documento']
    datos = getSIDEAP(tipo,numero)
    modulos = [x.nombre for x in request.user.estado.all()]
    return render(request,'postulante/create.html', {'tipo_documento': tipo_documento, 'respuesta': datos, 'modulos': modulos })

def nuevo_guardar(request):
    modulos = [x.nombre for x in request.user.estado.all()]
    p = radicacion_postulante(
        usuario=request.user,
        idpersonasideap =request.POST['idPersonaSIDEAP'],
        param_tipo_documento = 1,
        param_tipo_documento_text =request.POST['idTipoDocumento'],
        numero_documento =request.POST['numDocumento'],
        primer_nombre =request.POST['primerNom'],
        segundo_nombre =request.POST['otroNom'],
        primer_apellido =request.POST['primerApellido'],
        segundo_apellido =request.POST['segundoApellido'],
        param_codsexopersona =1,
        param_codsexopersona_text =request.POST['codSexoPersona'],
        id_pais_nacimiento =request.POST['idPaisNacimiento'],
        id_municipio_nacimiento =request.POST['idMunicipioNacimiento'],
        fecha_nacimiento = request.POST['fechaNacimiento'],
        tiene_libreta_militar =request.POST['tieneLibretaMilitar'],
        direccion_residencia =request.POST['direccionResidencia'],
        num_telefono_domicilio =request.POST['numTelefonoDomicilio'],
        correoelectronicopersonal =request.POST['correoElectronicoPersonal'],
    )

    mensaje_respuesta = "Se ha registrado el postulante y enviado correo para el cargue de documentos"
    #enviar el servicio de apolohv
    p.save()
    respuesta = setUsuarioPostulanteApolohv(p)    
    print("la respuesta fue://"+respuesta+"//")
    if respuesta=="1":       
        subject = 'Solicitud de carga de documentos'
        message = 'cargue sus documentos en el sistema APOLO ingresando a la siguiente direccion: ' + APOLOHV_URL
        message += ' <br/>Utilice el siguiente nombre de usuario: ' + p.correoelectronicopersonal + " y la siguiente clave:" + p.numero_documento
        recepient = str(request.POST['correoElectronicoPersonal'])
        enviar_correo(subject, message, recepient)
        # send_mail(subject,
        #           message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        #return render(request, 'subscribe/success.html', {'recepient': recepient})
    else:
        p.delete()
        mensaje_respuesta = respuesta

    estado = Estado.objects.filter(nombre="CREACION_RH").first()
    if request.user.is_superuser:
        postulantes = radicacion_postulante.objects.filter(estado=estado)
    else:
        postulantes = radicacion_postulante.objects.filter(usuario=request.user, estado=estado)
    return render(request,'postulante/list.html', {'postulantes' : postulantes , 'estados_postulantes': estados_postulantes,
                                                   'mensaje_respuesta' : mensaje_respuesta, 'modulos': modulos} )


def getSIDEAP(p_tipo_documento,p_numero_documento):
    import requests, json
    url_servicio = SIDEAP_URL#"http://preproduccion.serviciocivil.gov.co:8585/sideapInteroperabilidad/webresourcesJSON/sdis/obtenerDatosBasicosSDIS"
    key_servicio = SIDEAP_KEY #"9DBD932AB4D1308A3332C5181B2242F3BDD21408DE201FA2A3C261DE5370BE89"
    usuario_servicio = SIDEAP_USER #"PRUEBAS"
    respuesta = requests.get(url_servicio ,
                             headers = {"tipoDocumento":p_tipo_documento,
                                        "numeroDocumento":p_numero_documento,
                                        "key":key_servicio,
                                        "usuario":usuario_servicio,})
    if respuesta.text:
        data = json.loads(respuesta.text)
        return data
    else:
        return []


def setUsuarioPostulanteApolohv(p_persona):
    import requests, json
    apolohv_url_str = APOLOHV_URL
    url_str= "{0}/create_user_from_apolo?tipo_documento={1}&numero_documento={2}&id_sideap={3}&id_apolo={4}&correo={5}&primer_nombre={6}&primer_apellido={7}".format(
        apolohv_url_str ,
        p_persona.param_tipo_documento_text,
        p_persona.numero_documento,
        p_persona.idpersonasideap,
        p_persona.id,
        p_persona.correoelectronicopersonal,
        p_persona.primer_nombre,
        p_persona.primer_apellido,
    )

    url_servicio =    url_str
    # url_servicio = APOLOHV_URL + "/create_user_from_apolo?tipo_documento="+p_persona.param_tipo_documento_text+"&numero_documento="+p_persona.numero_documento+"&id_sideap="+p_persona.idpersonasideap+"&id_apolo="+p_persona.id+"&correo="+p_persona.correoelectronicopersonal+"&primer_nombre="+p_persona.primer_nombre+"&primer_apellido="+p_persona.primer_apellido

    respuesta = requests.get(url_servicio, data = {
        'tipo_documento' : p_persona.param_tipo_documento_text,
        'numero_documento' : p_persona.numero_documento,
        'correo': p_persona.correoelectronicopersonal,
    })

    if respuesta.text:
        data = respuesta.text
        return data
    else:
        return []

def cambiar_estado_archivo(id_archivo, id_estado):
    import requests, json

    url_servicio = APOLOHV_URL + "/cambiar_estado_archivo?id_archivo="+id_archivo+"&id_estado="+str(id_estado)

    respuesta = requests.get(url_servicio, data = {})

    if respuesta.text:
        data = respuesta.text
        return data
    else:
        return []

def cambiar_estado_postulante(p_correo, p_id_estado,p_mensaje, p_remitente ):
    import requests, json

    if int(p_id_estado) == 3:
        subject = 'Documentos enviados para subsanación'
        message = 'Tiene documentos pendientes de subsanar, por favor ingrese a APOLO utilizando la siguiente direccion: ' + APOLOHV_URL
        message += ' <br/>Actualice los documentos respectivos de acuerdo con las observaciones realizadas'
        enviar_correo(subject, message, p_correo)
    
    url_servicio = APOLOHV_URL + "/cambiar_estado_postulante?id_estado="+str(p_id_estado)+"&correo="+p_correo+"&mensaje="+p_mensaje+"&remitente="+p_remitente

    respuesta = requests.get(url_servicio, data = {})

    if respuesta.text:
        data = respuesta.text
        return data
    else:
        return []

@csrf_exempt 
def actualizar_estado_postulante(request):
    import traceback
    mensaje = 1 # "El usuario ha sido creado de manera correcta en Apolo HV"
    
    correo = request.GET['correo']
    nuevoestado = request.GET['id_estado']
    id_directorio_az = request.GET['id_directorio_az']

    try:
        p = radicacion_postulante.objects.get(correoelectronicopersonal = correo )
        p.id_estado = int(nuevoestado)
        p.id_directorio_azdigital = id_directorio_az
        p.save()
    except Exception as e:
        trace_back = traceback.format_exc()
        mensaje = "ERROR NO CONTROLADO, POR FAVOR ENVÍE ESTE PANTALLAZO AL ADMINISTRADOR DEL SISTEMA:" + str(e)+ " >>>>>> " + str(trace_back)
        #mensaje = e # '%s (%s)' % (e.message, type(e))
    return HttpResponse(mensaje)



def lista_postulantes(request):
    estado = Estado.objects.filter(nombre="CREACION_RH").first()
    modulos = [x.nombre for x in request.user.estado.all()]
    if request.user.is_superuser:
        postulantes = radicacion_postulante.objects.filter(estado=estado)
    else:
        postulantes = radicacion_postulante.objects.filter(usuario=request.user,estado=estado)
    # postulantes = getListaPostulante()

    return render(request,'postulante/list.html', {'postulantes' : postulantes, 'estados_postulantes': estados_postulantes, 'modulos': modulos})

def documentos_postulante(request, correo):

    class proceso:
        nombre_contratista = ""
        cedula_contratista = ""
        numero_cdp = ""
        valor_cdp = ""
        valor_contrato = ""
        proyecto =""
        objeto = ""

    msg="1"
    modulos = [x.nombre for x in request.user.estado.all()]
    postulante = radicacion_postulante.objects.get(correoelectronicopersonal=correo)
    mensajes = getMensajesFromPostulante(correo)
    documentos = getDocumentosFromPostulante(correo)
    cdps = radicacion_cdp.objects.filter(id_radicacion_postulante=postulante.id)
    total = cdps.aggregate(Sum('valor_afectacion'))
    # AQUI SE CREA UN NUEVO PROCESO PARA RECURSO HUMANO
    if request.method == "POST":
        boton = request.POST.get('enviar')

        if boton == "crear_proceso":
            estado = Estado.objects.filter(nombre="REVISION").first()
            postulante.estado = estado
            postulante.save()
            proc = postulante.proceso
            asignar(proc.id, ProcesoEstados.REVISION)
            arraycdp = ""
            for cdp in cdps:
                arraycdp = arraycdp + "," + str(cdp.numero_cdp)
                cdp.proceso = proc
                cdp.save()
            arraycdp = arraycdp[1:]
            proc.numero_cdp = arraycdp
            proc.save()
            proceso.numero_de_proceso = proc.numero_de_proceso
            proceso.nombre_contratista = proc.nombre_contratista
            proceso.cedula_contratista = proc.cedula_contratista
            proceso.numero_cdp = arraycdp
            proceso.valor_cdp = proc.valor_cdp
            proceso.valor_contrato = proc.valor_contrato
            proceso.proyecto = proc.proyecto_id
            proceso.objeto = proc.objeto
            return render(request, 'postulante/success.html', {'proceso': proceso, 'postulante': postulante,
                                                               'modulos': modulos})

        if boton == "buscar_cdp":
            vigencia_plan = request.POST['vigencia_plan']
            numero = request.POST['numero_cdp']
            vigencia_cdp = request.POST['vigencia_cdp']
            datos = get_cdp_from_paa(vigencia_plan, numero, vigencia_cdp)
            return render(request, 'postulante/documentos.html',
                          {'respuesta': datos, 'documentos': documentos, 'postulante': postulante, 'mensajes': mensajes,'modulos': modulos,
                           'estados_postulantes': estados_postulantes, 'cdps': cdps, 'total': total, 'proceso': proceso, 'vigencia_plan':vigencia_plan, 'vigencia_cdp': vigencia_cdp})

        if boton == "guardar_cdp":
            valor_cdp = request.POST['ValorCDP'].replace(",", ".")
            p = radicacion_cdp(
                usuario=request.user,
                numero_cdp=request.POST['NumeroCDP'],
                vigencia_cdp=request.POST['VigenciaCDP'],
                vigencia_plan_cdp=request.POST['VigenciaPAA'],
                valor_cdp=float(valor_cdp),
                honorarios=float(request.POST['honorarios']),
                valor_contrato=float(request.POST['valor_contrato']),
                valor_afectacion=float(request.POST['valor_afectacion']),
                codigo_proyecto=request.POST['CodProyecto'],
                id_cupo_paa=request.POST['IdCupo'],
                descripcion_cupo=request.POST['DescripcionCupo'],
                descripcion_objeto=request.POST['ObjetoDelContrato'],
                nombre_proyecto=request.POST['NompreProyecto'],
                nuemero_caso='',  # request.POST['NumeroDeCaso'],
                id_radicacion_postulante=postulante.id,
                idpersonasideap=postulante.idpersonasideap,
            )
            p.save()
            mensaje_respuesta = "Se ha registrado el CDP"
            cdps = radicacion_cdp.objects.filter(id_radicacion_postulante=postulante.id)

            if postulante.proceso is None:
                proy = Proyecto.objects.filter(numero=cdps.first().codigo_proyecto).first()
                proc = Proceso.objects.create(
                    nombre_contratista=postulante.primer_nombre + " " + postulante.segundo_nombre + " " + postulante.primer_apellido + " " + postulante.segundo_apellido,
                    cedula_contratista=postulante.numero_documento,
                    numero_cdp=cdps.first().numero_cdp,
                    valor_cdp=cdps.first().valor_cdp,
                    valor_contrato=cdps.first().valor_contrato,
                    proyecto=proy,
                    objeto=cdps.first().descripcion_objeto, )
                proc.numero_de_proceso = "SDIS-" + str(proc.id)
                proc.save()
                postulante.proceso = proc
                postulante.save()
                mensaje_respuesta = "Se ha registrado el CDP u creado el proceso " + proc.numero_de_proceso
                #TENER CUIDADO CUANDO SE BORRAN LOS CDPS Y QUEDA SIN CDP EL PROCESO


            total = cdps.aggregate(Sum('valor_afectacion'))
            return render(request, 'postulante/documentos.html',
                          {'mensaje_respuesta':mensaje_respuesta, 'documentos': documentos, 'postulante': postulante, 'mensajes': mensajes,
                           'estados_postulantes': estados_postulantes, 'cdps': cdps, 'total': total, 'proceso': proceso, 'modulos': modulos})

        if boton.startswith("borrar"):
            idcdp = int(boton.lstrip("borrar"))
            cdpborrar = radicacion_cdp.objects.filter(id=idcdp)
            mensaje_respuesta = "Se elimino afectación por $" + str(cdpborrar.first().valor_afectacion)
            cdpborrar.delete()
            cdps = radicacion_cdp.objects.filter(id_radicacion_postulante=postulante.id)
            return render(request, 'postulante/documentos.html',
                          {'mensaje_respuesta': mensaje_respuesta, 'documentos': documentos, 'postulante': postulante,
                           'mensajes': mensajes,'modulos': modulos,
                           'estados_postulantes': estados_postulantes, 'cdps': cdps, 'total': total, 'proceso': proceso})

        if boton == "guardar":
            current_user = request.user
            p_id_estado = 2 #request.POST['nuevo_estado']
            p_mensaje = request.POST['mensaje']
            p_remitente = current_user.username
            for docs in request.POST.getlist('id_param_archivo'):
                nuevo_estado = request.POST['nuevo_estado_documento_'+str(docs)]
                id_archivo = request.POST['id_archivo_'+str(docs)]
                if int(id_archivo) > 0 :
                    cambiar_estado_archivo(id_archivo,nuevo_estado)
                if int(nuevo_estado) == 3:
                    p_id_estado = 3

            cambiar_estado_postulante(correo, p_id_estado,p_mensaje, p_remitente)

    documentos = getDocumentosFromPostulante(correo)
    # print(respuesta)
    return render(request,'postulante/documentos.html',{'documentos': documentos, 'postulante': postulante, 'mensajes':mensajes,
                                                        'estados_postulantes': estados_postulantes, 'cdps': cdps, 'total': total,
                                                        'proceso': proceso, 'modulos': modulos})

def getMensajesFromPostulante(p_correo):
    import requests, json
    url_servicio = APOLOHV_URL + "/get_mensajes_postulantes?correo="+p_correo
    respuesta = requests.get(url_servicio ,  data = {} )
    if respuesta.text:
        data = json.loads(respuesta.text)
        return data
    else:
        return []

def getDocumentosFromPostulante(p_correo):
    import requests, json
    url_servicio = APOLOHV_URL + "/get_lista_documentos_postulantes?correo="+p_correo
    respuesta = requests.get(url_servicio ,  data = {} )
    if respuesta.text:
        data = json.loads(respuesta.text)
        return data
    else:
        return []

def getListaPostulante():
    import requests, json
    url_servicio = APOLOHV_URL + "/get_lista_postulantes"
    respuesta = requests.get(url_servicio ,  data = {} )
    if respuesta.text:
        data = json.loads(respuesta.text)
        return data
    else:
        return []

def fakeservices(request):
    return render(request,'postulante/fakeservices.html',{})