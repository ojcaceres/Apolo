from django.urls import path

from apps.contratacion.views.views_perfeccionamiento import ListarPerfeccionamiento, EditarPerfeccionamiento
from apps.contratacion.views.views_financiera import ListarTramitefinanciera, EditarTramitefinanciera
from apps.contratacion.views.views_tramite_crp import ListarFirmado, ListarSolicitudCRP, EditarFirmado, EditarSolicitudCRP, ListarCRPDevuelto
from apps.contratacion.views.views_radicacion import CreacionProcesoRadicacion, ListarRevision, \
    EditarRadicacion, ListarRevisionMod, EditarModificaciones
from apps.contratacion.views.views_alistamiento import EditarRevisar, ListarRevisar, ListarPrimerFlujo, \
    EditarPrimerFlujo, EditarRevisarMod, ListarRevisarMod, ListarSubsanacion, EditarSubsanacion
from apps.contratacion.views.views_numeracion import ListarNumeracion, EditarNumeracion
from apps.contratacion.views.views_secop_publicacion import ListarSecopPublicacion, EditarSecopPublicacion
from apps.contratacion.views.views_secop_flujo import ListarSecopRevisar, ListarSecopSegundoFlujo, EditarSecopRevisar,\
    EditarSecopSegundoFlujo, EditarSecop_Firma , ListarSecop_Firma
from apps.contratacion.views.views_modificaciones import CreacionModificacion


urlpatterns = (
    # Radicacion
    path("radicacion/nuevo/", CreacionProcesoRadicacion.as_view(), name="RadicacionProcesoCreateView"),
    path('radicacion/revision/', ListarRevision.as_view(), name="ListarRevision"),
    path('radicacion/revision/<int:pk>', EditarRadicacion.as_view(), name='radicado_editar'),

    # Alistamiento
    path('alistamiento/revisar/', ListarRevisar.as_view(), name="ListarRevisar"),
    path('alistamiento/revisar/<int:pk>', EditarRevisar.as_view(), name='RevisarUpdate'),

    path('alistamiento/primer-flujo/', ListarPrimerFlujo.as_view(), name="ListarPrimerFlujo"),
    path('alistamiento/primer-flujo/<int:pk>', EditarPrimerFlujo.as_view(), name='PrimerFlujoUpdate'),

    path('alistamiento/revisar_mod/', ListarRevisarMod.as_view(), name="ListarRevisar_mod"),
    path('alistamiento/revisar_mod/<int:pk>', EditarRevisarMod.as_view(), name='RevisarUpdate_mod'),

    path('alistamiento/subsanacion/', ListarSubsanacion.as_view(), name="ListarSubsanacion"),
    path('alistamiento/subsanacion/<int:pk>', EditarSubsanacion.as_view(), name='RevisarSubsanacion'),

    # Numeracion
    path('numeracion/', ListarNumeracion.as_view(), name="listar-numeracion"),
    path('numeracion/<int:pk>', EditarNumeracion.as_view(), name='numeracion_update'),

    # Secop publicacion
    path('secop-publicacion/', ListarSecopPublicacion.as_view(), name="listar_activos"),
    path('secop-publicacion/<int:pk>', EditarSecopPublicacion.as_view(), name='activos_update'),

    # Secop flujo
    path('secop-flujos/revisar/', ListarSecopRevisar.as_view(), name="listar_revisar"),
    path('secop-flujos/revisar/<int:pk>', EditarSecopRevisar.as_view(), name='seco_revisar_update'),

    path('secop-flujos/segundo-flujo/', ListarSecopSegundoFlujo.as_view(), name="listar_segundo_flujo"),
    path('secop-flujos/segundo-flujo/<int:pk>', EditarSecopSegundoFlujo.as_view(), name='segundo_flujo_update'),

    path('secop-flujos/secop-firma/', ListarSecop_Firma.as_view(), name="listar_secop-firma"),
    path('secop-flujos/secop-firma/<int:pk>', EditarSecop_Firma.as_view(), name='secop-firma_update'),

    # Trámite CRP
    path('tramite-crp/firmados/', ListarFirmado.as_view(), name="listar_firmado"),
    path('tramite-crp/firmados/<int:pk>', EditarFirmado.as_view(), name="firmado_update"),

    path('tramite-crp/solicitud-crp/', ListarSolicitudCRP.as_view(), name="listar_solicitud_crp"),
    path('tramite-crp/solicitud-crp/<int:pk>', EditarSolicitudCRP.as_view(), name="firmado_update"),

    path('tramite-crp/devueltos/', ListarCRPDevuelto.as_view(), name="listar_crp_devueltos"),

    # Financiera
    path('financiera/tramite/', ListarTramitefinanciera.as_view(), name="ListarTramitefinanciera"),
    path('financiera/tramite/<int:pk>', EditarTramitefinanciera.as_view(), name="TramitefinancieraUpdate"),

    # Perfeccionamiento
    path('perfeccionamiento/', ListarPerfeccionamiento.as_view(), name="ListarPerfeccionamiento"),
    path('perfeccionamiento/<int:pk>', EditarPerfeccionamiento.as_view(), name="perfeccionamiento_update"),

    # Modificaciones
    path('modificaciones/creacion', CreacionModificacion, name="Creacion"),
    path('modificaciones/revision/', ListarRevisionMod.as_view(), name="ListarRevisionMod"),
    path('radicacion/editar_modificaciones/<int:pk>', EditarModificaciones.as_view(), name="EditarModificaciones"),

)