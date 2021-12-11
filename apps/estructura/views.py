from django.views import generic
from . import models
from . import forms


class proyectoListView(generic.ListView):
    model = models.Proyecto
    form_class = forms.proyectoForm


class proyectoCreateView(generic.CreateView):
    model = models.Proyecto
    form_class = forms.proyectoForm


class proyectoDetailView(generic.DetailView):
    model = models.Proyecto
    form_class = forms.proyectoForm


class proyectoUpdateView(generic.UpdateView):
    model = models.Proyecto
    form_class = forms.proyectoForm
    pk_url_kwarg = "pk"


class moduloListView(generic.ListView):
    model = models.Modulo
    form_class = forms.moduloForm


class moduloCreateView(generic.CreateView):
    model = models.Modulo
    form_class = forms.moduloForm


class moduloDetailView(generic.DetailView):
    model = models.Modulo
    form_class = forms.moduloForm


class moduloUpdateView(generic.UpdateView):
    model = models.Modulo
    form_class = forms.moduloForm
    pk_url_kwarg = "pk"


class estadoListView(generic.ListView):
    model = models.Estado
    form_class = forms.estadoForm


class estadoCreateView(generic.CreateView):
    model = models.Estado
    form_class = forms.estadoForm


class estadoDetailView(generic.DetailView):
    model = models.Estado
    form_class = forms.estadoForm


class estadoUpdateView(generic.UpdateView):
    model = models.Estado
    form_class = forms.estadoForm
    pk_url_kwarg = "pk"
