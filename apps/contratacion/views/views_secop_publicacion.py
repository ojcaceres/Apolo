from apps.contratacion.views.views_genericos import EditarProceso, ListarProcesosMixin
from django.urls import reverse_lazy
from apps.contratacion.models import Proceso, ProcesoEstados
from apps.contratacion.flow import getNext, getBack

class ListarSecopPublicacion(ListarProcesosMixin):
    estado = ProcesoEstados.SECOP_PUBLICACION


class EditarSecopPublicacion(EditarProceso):
    success_url = reverse_lazy('listar_activos')