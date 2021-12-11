from apps.contratacion.forms import TramiteCRPForm
from django.urls import reverse_lazy
from apps.contratacion.models import Proceso, ProcesoEstados
from apps.contratacion.views.views_genericos import EditarProceso, ListarProcesosMixin

class ListarFirmado(ListarProcesosMixin):
    estado = ProcesoEstados.FIRMADO


class EditarFirmado(EditarProceso):
    form_class = TramiteCRPForm
    success_url = reverse_lazy('listar_firmado')


class ListarSolicitudCRP(ListarProcesosMixin):
    estado = ProcesoEstados.SOLICITUD_CRP


class EditarSolicitudCRP(EditarProceso):
    form_class = TramiteCRPForm
    success_url = reverse_lazy('listar_solicitud_crp')


class ListarCRPDevuelto(ListarProcesosMixin):
    estado = ProcesoEstados.CRP_DEVUELTO

