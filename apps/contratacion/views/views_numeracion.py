from apps.contratacion.views.views_genericos import EditarProceso, ListarProcesosMixin
from apps.contratacion.forms import NumeracionForm
from django.urls import reverse_lazy
from apps.contratacion.models import ProcesoEstados

class ListarNumeracion(ListarProcesosMixin):
    estado = ProcesoEstados.NUMERACION_CONTRATO


class EditarNumeracion(EditarProceso):
    form_class = NumeracionForm
    success_url = reverse_lazy('listar-numeracion')
