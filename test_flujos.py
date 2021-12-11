import django, os

os.environ['DJANGO_SETTINGS_MODULE'] = 'Apolo.settings'
django.setup()

from apps.contratacion.models import ProcesoEstados
from apps.contratacion.lists_flow import getListFlow

variables = getListFlow(ProcesoEstados.REVISAR)
print(variables["TITULO"])