import random

from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.db.models import Sum

from apps.contratacion.models import Proceso, ProcesoEstados, UsuariosProcesos
from apps.contratacion.forms import ProcesoGeneralForm
from apps.autenticacion.models import USUARIO
from apps.postulantes.models import radicacion_cdp
from apps.estructura.models import Estado
from apps.contratacion.flow import getFlow
from apps.contratacion.lists_flow import getListFlow



def asignar(pk_proceso: int, next_estado: ProcesoEstados, novedad:str=None, usuario_id: int=None, devolver: bool=False):
    proc = Proceso.objects.get(id=pk_proceso)

    #Revisar si fue devuelto
    if proc.estado_devolucion == proc.estado:
        proc.devuelto = False
    if devolver:
        proc.devuelto = devolver
        proc.estado_devolucion=proc.estado
    estado = Estado.objects.filter(nombre=next_estado.value).first()


    #En caso de ser asignado un Usuario ej: asignado a subsanacion
    if usuario_id is not None:
        usuario = USUARIO.objects.get(id=usuario_id)
    else:
            #Busque si fue asignado un usuario_proceso para el estado especial para volver a Revisar en caso de subsanacion
            usuario_proceso = UsuariosProcesos.objects.filter(usuario__is_active=True).filter(proceso=proc) \
                .filter(estado=estado).first()
            print("buscando si existe usuario proceso en el mismo estado")
            #asignele un usuario que ya haya sido asignado en el modulo a otro estado
            if not usuario_proceso:
                usuario_proceso = UsuariosProcesos.objects.filter(usuario__is_active=True).filter(proceso=proc) \
                .filter(estado__modulo=estado.modulo).first()
                print("buscando dentro del mismo modulo")
            if usuario_proceso:
                #si existe entonces asigne usuario
                usuario = usuario_proceso.usuario
                print(usuario, " ya tenia el proceso", proc.numero_de_proceso, " asignado en estado", estado)
            else:
                #Si no Existe un usuario busque los usuarios disponibles para el estado
                usuarios = USUARIO.objects.filter(estado=estado).filter(is_active=True)
                if usuarios:
                    #Asigne al Usuario Proceso un usuario Random
                    usuario = random.choice(usuarios)
                    print(usuario, " acaba de ser asignado al proceso", proc.numero_de_proceso, " en estado", estado)
                else:
                    #Este error rompe el codigo porque al no haber un usuario asignado nadie puede trabajar sobre la estacion actual
                    print("no hay usuarios disponibles")
                    usuario = None
    proc.usuario = usuario
    proc.estado = estado
    proc.save()
    print("grabado",usuario,proc, novedad,estado)
    UsuariosProcesos.objects.create(
                usuario = usuario,
                proceso=proc,
                novedad=novedad,
                estado=estado
            )


class CustomView(View):
    template_params = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['modulos'] = ','.join([x.nombre for x in self.request.user.estado.all()])
        context['modulos'] = [x.nombre for x in self.request.user.estado.all()]
        for key in self.template_params:
            context[key] = self.template_params[key]
        return context


class ListarProcesosMixin(
    CustomView,
    LoginRequiredMixin, generic.ListView, ):
    model = Proceso
    paginate_by = 100
    estado = None
    context_object_name = 'procesos_list'
    template_name = 'genericos/listar_procesos.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser and not any(
                [estado for estado in request.user.estado.all() if self.estado.value == estado.nombre]):
            return HttpResponseRedirect('/')
        else:
            return super(ListarProcesosMixin, self).dispatch(request=request, *args, **kwargs)

    def get_queryset(self):
        if self.request.user.is_superuser:
            queryset = Proceso.objects.filter(
                estado__nombre=self.estado
            ).order_by('-devuelto','-fecha_final')
            if self.request.GET.get("no_proceso"):
                no_proceso = self.request.GET.get("no_proceso")
                queryset = Proceso.objects.filter(numero_de_proceso__icontains=no_proceso, estado=self.estado).order_by('-devuelto','-fecha_final')
        else:
            queryset = Proceso.objects.filter(
                usuario=self.request.user,
                estado__nombre=self.estado
            ).order_by('devuelto','fecha_final')
            if self.request.GET.get("no_proceso"):
                no_proceso = self.request.GET.get("no_proceso")
                queryset = Proceso.objects.filter(numero_de_proceso__icontains=no_proceso, usuario=self.request.user, estado=self.estado).order_by('devuelto','fecha_final')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ListarProcesosMixin, self).get_context_data(**kwargs)
        variables = getListFlow(self.estado)
        context.update({'variables': variables})
        return context

class EditarProceso(CustomView,
                    LoginRequiredMixin,
                    generic.UpdateView):
    model = Proceso
    template_params = {
        'show_back_buttons': True
    }
    model = Proceso
    form_class = ProcesoGeneralForm
    pk_url_kwarg = "pk"
    success_url = reverse_lazy('lista-revisar')
    template_name = "genericos/editar_proceso.html"
    novedad = ""
    usuario = None
    proc = None

    def dispatch(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        self.proc = Proceso.objects.get(id=pk)
        variablesFlow=getFlow(self.proc.modificacion, self.proc.estado.nombre)
        self.next_state = variablesFlow["next"]
        if self.next_state == ProcesoEstados.NUMERACION_CONTRATO and self.proc.devuelto:
            self.next_state = ProcesoEstados.SECOP_PUBLICACION
        self.back_state = variablesFlow["back"]
        #TERCER BOTON
        if "action" in variablesFlow:
            self.action_state = variablesFlow["action"]
        else:
            self.action_state = None

        usuario_proceso = UsuariosProcesos.objects.filter(proceso=self.proc).first()
        if usuario_proceso : self.novedad = usuario_proceso.novedad
        return super(EditarProceso, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(EditarProceso, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        cdps = radicacion_cdp.objects.filter(proceso_id=pk)
        historial = UsuariosProcesos.objects.filter(proceso_id=pk)
        total = cdps.aggregate(Sum('valor_afectacion'))
        context.update({'next_state': self.next_state, 'back_state': self.back_state,
                        'action_state': self.action_state, 'cdps': cdps, 'total': total, 'registros': historial,
                        'novedad_previa': self.novedad, 'proceso':self.proc})
        return context

    def pre_post(self, request, *args, **kwargs):
        pass

    def post(self, request, pk, *args, **kwargs):
        request.POST = request.POST.copy()
        self.pre_post(request, *args, **kwargs)
        f = self.form_class(request.POST)

        if f.is_valid():
            print("paso como valida")
            self.novedad=request.POST['novedad']
            if request.POST['action'] == 'Next':
                NEXT = self.next_state
                asignar(pk, NEXT, self.novedad)

            elif request.POST['action'] == 'Action':
                NEXT = self.action_state
                asignar(pk, NEXT, self.novedad)

            elif request.POST['action'] == 'Back':

                NEXT = self.back_state
                if "usuario" in request.POST:
                    asignar(pk, NEXT, self.novedad, request.POST['usuario'], True)
                else:
                    print("deberia ser true")
                    asignar(pk, NEXT, self.novedad, None, True)

            elif request.POST['action'] == 'Save':
                NEXT = ProcesoEstados.__getitem__(request.POST['estado'])
                asignar(pk, NEXT, self.novedad)



            request.POST['estado'] = NEXT.value if type(NEXT) is ProcesoEstados else NEXT

        return super(EditarProceso, self).post(request, **kwargs)