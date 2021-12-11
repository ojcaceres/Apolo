from apps.contratacion.views.views_genericos import EditarProceso, ListarProcesosMixin
from django.urls import reverse_lazy
from apps.autenticacion.models import USUARIO
from apps.contratacion.models import Proceso, ProcesoEstados

class ListarPrimerFlujo(ListarProcesosMixin):
    estado = ProcesoEstados.PRIMER_FLUJO


class ListarRevisar(ListarProcesosMixin):
    estado = ProcesoEstados.REVISAR


class ListarRevisarMod(ListarProcesosMixin):
    estado = ProcesoEstados.REVISARMOD


class ListarSubsanacion(ListarProcesosMixin):
    estado = ProcesoEstados.SUBSANACION


class EditarSubsanacion(EditarProceso):
    success_url = reverse_lazy('ListarSubsanacion')
    template_name = "alistamiento/editar_subsanacion.html"


class EditarRevisar(EditarProceso):
    success_url = reverse_lazy('ListarRevisar')
    template_name = "alistamiento/editar_revisar_primerflujo_aprobacion.html"

    def get_context_data(self, **kwargs):          
        context = super(EditarRevisar, self).get_context_data(**kwargs)
        usersub_list = USUARIO.objects.filter(estado__nombre="SUBSANACION") \
                .filter(is_active=True).order_by('first_name')                
        context.update({'usersub_list': usersub_list})
        return context


class EditarPrimerFlujo(EditarProceso):
    success_url = reverse_lazy('ListarPrimerFlujo')
    template_name = "alistamiento/editar_revisar_primerflujo_aprobacion.html"

    def get_context_data(self, **kwargs):          
        context = super(EditarPrimerFlujo, self).get_context_data(**kwargs)
        usersub_list = USUARIO.objects.filter(estado__nombre="SUBSANACION") \
                .filter(is_active=True).order_by('first_name')
        context.update({'usersub_list': usersub_list})
        return context


class EditarRevisarMod(EditarProceso):
    success_url = reverse_lazy('ListarRevisar')
    template_name = "alistamiento/editar_revisar_primerflujo_aprobacion.html"

    def get_context_data(self, **kwargs):
        context = super(EditarRevisarMod, self).get_context_data(**kwargs)
        usersub_list = USUARIO.objects.filter(estado__nombre="SUBSANACION") \
                .filter(is_active=True).order_by('first_name')
        context.update({'usersub_list': usersub_list})
        return context
