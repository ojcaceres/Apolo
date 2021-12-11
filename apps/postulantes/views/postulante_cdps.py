from django.shortcuts import render
from apps.postulantes.views.paa_services import get_cdp_from_paa
from apps.postulantes.models import radicacion_postulante, radicacion_cdp, parametricas






#Vistas nuevo CDP
def nuevo_cdp(request):
    if 'buscar' in request.POST:
        vigencia_plan = request.POST['vigencia_plan']
        numero = request.POST['numero_cdp']
        vigencia_cdp = request.POST['vigencia_cdp']
        print(numero, vigencia_plan, vigencia_cdp)
        datos = get_cdp_from_paa(vigencia_plan, numero, vigencia_cdp)
        return render(request,'postulante/create_cdp.html',{'respuesta':datos, 'vigencia_plan':vigencia_plan,'vigencia_cdp': vigencia_cdp })
    if 'guardar' in request.POST:
        valor_cdp = request.POST['ValorCDP'].replace(",",".")
        p = radicacion_cdp(
            usuario=request.user,
            numero_cdp  =request.POST['NumeroCDP'],
            vigencia_cdp  =request.POST['VigenciaCDP'],
            vigencia_plan_cdp =request.POST['VigenciaPAA'],
            valor_cdp =float(valor_cdp),
            honorarios  = float(request.POST['honorarios']),
            valor_contrato = float(request.POST['valor_contrato']),
            valor_afectacion  = float(request.POST['valor_afectacion']),
            codigo_proyecto  =request.POST['CodProyecto'],
            id_cupo_paa =request.POST['IdCupo'],
            descripcion_cupo =request.POST['DescripcionCupo'],
            descripcion_objeto=request.POST['ObjetoDelContrato'],
            nombre_proyecto=request.POST['NompreProyecto'],
            nuemero_caso = '',#request.POST['NumeroDeCaso'],
            id_radicacion_postulante = 0 , #request.POST['idPersonaSIDEAP'],
            idpersonasideap = 0 , # request.POST['idPersonaSIDEAP'],

        )
        p.save()
        mensaje_respuesta="Se ha registrado el CDP"
        lista_cdps = radicacion_cdp.objects.all()
        return render(request,'postulante/list_cdp.html',{'mensaje_respuesta':mensaje_respuesta, 'cdps':lista_cdps})


    print('numero')
    return render(request,'postulante/create_cdp.html',{})


#Vistas nuevo CDP
def lista_cdp(request):

    if request.user.is_superuser:
        lista_cdps = radicacion_cdp.objects.all()
    else:
        lista_cdps = radicacion_cdp.objects.filter(usuario=request.user)

    return render(request,'postulante/list_cdp.html',{ 'cdps':lista_cdps})

def cdp_to_postulante(request,id_cdp):
    if 'buscar' in request.POST:
        postulante = radicacion_postulante.objects.filter(numero_documento = request.POST['cedula_postulante']).first()
        cdp = radicacion_cdp.objects.get(id = id_cdp)
        return render(request,'postulante/create_cdp_to_postulante.html',{ 'cdp':cdp, 'postulante':postulante})
    if 'asignar' in request.POST:
        cdp = radicacion_cdp.objects.get(id = id_cdp)
        postulante = radicacion_postulante.objects.get(id = request.POST['id_radicacion_postulante'])
        cdp.id_radicacion_postulante = postulante.id
        cdp.idPersonaSIDEAP = postulante.idpersonasideap
        cdp.save() 
        lista_cdps = radicacion_cdp.objects.all()
        mensaje_respuesta = "Se ha asignado la persona al cupo"
        return render(request,'postulante/list_cdp.html',{'mensaje_respuesta':mensaje_respuesta, 'cdps':lista_cdps})   
    
    cdp = radicacion_cdp.objects.get(id = id_cdp)
    return render(request,'postulante/create_cdp_to_postulante.html',{ 'cdp':cdp})

def documentos_proceso(request, id_cdp):
    documentos = parametricas.objects.filter(categoria = 'documento_proceso_cargar').order_by('orden')
    cdp = radicacion_cdp.objects.get(id = id_cdp)

    return render(request,'postulante/documentos_proceso.html',{ 'documentos':documentos, 'cdp':cdp })
