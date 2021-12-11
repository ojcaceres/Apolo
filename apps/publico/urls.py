from django.conf.urls import url
from django.urls import path, include
from .views import RevisarProceso

urlpatterns = [
    url('consulta/', RevisarProceso)
]
