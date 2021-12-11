from apps.contratacion.views.views_genericos import EditarProceso, ListarProcesosMixin
from django.urls import reverse_lazy
from apps.contratacion.models import Proceso, ProcesoEstados


class ListarSecopRevisar(ListarProcesosMixin):
    estado = ProcesoEstados.SECOP_REVISAR


class EditarSecopRevisar(EditarProceso):
    success_url = reverse_lazy('listar_revisar')


class ListarSecopSegundoFlujo(ListarProcesosMixin):
    estado = ProcesoEstados.SEGUNDO_FLUJO


class EditarSecopSegundoFlujo(EditarProceso):
    success_url = reverse_lazy('listar_segundo_flujo')


class ListarSecop_Firma(ListarProcesosMixin):
    estado = ProcesoEstados.SECOP_FIRMA


class EditarSecop_Firma(EditarProceso):
    success_url = reverse_lazy('listar_secop-firma')