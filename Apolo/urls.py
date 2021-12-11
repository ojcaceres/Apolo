from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from apps.postulantes.views import postulante_views, postulante_cdps, postulante_documentos
from apps.postulantes.pdfviews import noplanta, estudiosprevios
from apps.contratacion.views import views_iops

urlpatterns = [
    path('publico/', include('apps.publico.urls')),
    path('estructura/', include('apps.estructura.urls')),
    path('contratacion/', include('apps.contratacion.urls')),
    path('admin/', admin.site.urls),
    path("", include("apps.autenticacion.urls")),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('iops', views_iops.iops_api, name='create_user_from_apolo'),
    path('postulante/lista', postulante_views.lista_postulantes, name='lista_postulantes'),
    path('postulante/noplanta', noplanta.NoPlantaPDF.as_view(), name="no_planta_pdf"),
    path('postulante/ep', estudiosprevios.EstudiosPreviosPDF.as_view(), name="estudios_previos_pdf"),
    path('postulante/nuevo', postulante_views.nuevo, name='nuevo_postulante'),
    path('postulante/documentos/<str:correo>', postulante_views.documentos_postulante, name='documentos_postulante'),
    path('postulante/nuevo_resultado', postulante_views.nuevo_resultado, name='nuevo_postulante_resultado'),
    path('postulante/nuevo_guardar', postulante_views.nuevo_guardar, name='nuevo_postulante_guardar'),
    path('postulante/fakeservices/PAA', postulante_views.fakeservices, name='fakeservices_paa'),
    path('postulante/actualizar_estado_postulante',postulante_views.actualizar_estado_postulante,name='actualizar_estado_postulante'),  

    path('cdp/nuevo', postulante_cdps.nuevo_cdp, name='nuevo_cdp'),
    path('cdp/list', postulante_cdps.lista_cdp, name='lista_cdp'),
    path('cdp/<str:id_cdp>/postulante', postulante_cdps.cdp_to_postulante, name='cdp_to_postulante'),
    path('cdp/<str:id_cdp>/documentos_proceso', postulante_cdps.documentos_proceso, name='documentos_proceso'),
    path('cdp/<str:id_cdp>/certificado_no_planta', postulante_documentos.certificado_no_planta, name='certificado_no_planta'),
    path('cdp/<str:id_cdp>/obligaciones_contratista', postulante_documentos.obligaciones_contratista, name='obligaciones_contratista'),
    path('cdp/<str:id_cdp>/certificado_no_planta_print', postulante_documentos.certificado_no_planta_print, name='certificado_no_planta_print'),
    path('cdp/<str:id_cdp>/certificado_idoneidad_print', postulante_documentos.certificado_idoneidad_print, name='certificado_idoneidad_print'),
    path('cdp/<str:id_cdp>/estudios_previos_print', postulante_documentos.estudios_previos_print, name='estudios_previos_print'),
]
