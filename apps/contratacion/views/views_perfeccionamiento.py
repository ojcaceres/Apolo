from apps.contratacion.views.views_genericos import EditarProceso, ListarProcesosMixin
from apps.contratacion.forms import NumeracionForm
from django.urls import reverse_lazy
from apps.contratacion.models import Proceso, ProcesoEstados


class ListarPerfeccionamiento(ListarProcesosMixin):
    estado = ProcesoEstados.PERFECCIONAMIENTO

class EditarPerfeccionamiento(EditarProceso):
    form_class = NumeracionForm
    success_url = reverse_lazy('ListarPerfeccionamiento')

