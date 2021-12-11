from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.contratacion.models import Proceso, ProcesoEstados
from apps.contratacion.views.views_genericos import EditarProceso, ListarProcesosMixin
from apps.contratacion.forms import CreateProcesoRadicacionForm, RadicacionForm
from django.urls import reverse_lazy


class ListarRevision(ListarProcesosMixin):
    estado = ProcesoEstados.REVISION


class ListarRevisionMod(ListarProcesosMixin):
    estado = ProcesoEstados.REVISIONMOD


class CreacionProcesoRadicacion(LoginRequiredMixin, generic.CreateView):
    model = Proceso
    form_class = CreateProcesoRadicacionForm
    success_url = reverse_lazy('ListarRevision')


class EditarRadicacion(EditarProceso):
    form_class = RadicacionForm
    success_url = reverse_lazy('ListarRevision')


class EditarModificaciones(EditarProceso):
    form_class = RadicacionForm
    success_url = reverse_lazy('ListarRevisionMod')
