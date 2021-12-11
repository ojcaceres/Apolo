import os
import sys
import django

import random

from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.db.models import Count, Min, Max, Avg


os.environ['DJANGO_SETTINGS_MODULE'] = 'Apolo.settings'
django.setup()


from apps.estructura.models import Estado, Modulo



Modulo.objects.create( nombre="CREACION" )

modulo = Modulo.objects.get(nombre="CREACION")
Estado.objects.create(
                    nombre="CREACION_RH",
                    modulo=modulo
                )


print("favor no ejecutar este proceso de nuevo")
