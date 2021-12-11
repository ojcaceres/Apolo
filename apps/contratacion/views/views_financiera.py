from apps.contratacion.views.views_genericos import EditarProceso, ListarProcesosMixin
from django.urls import reverse_lazy
from apps.contratacion.models import Proceso, ProcesoEstados


class ListarTramitefinanciera(ListarProcesosMixin):
    estado = ProcesoEstados.TRAMITE_FINANCIERA


class EditarTramitefinanciera(EditarProceso):
    success_url = reverse_lazy('ListarTramitefinanciera')