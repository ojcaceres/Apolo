from django.views import generic
from . import models
from . import forms


class PlanAnualListView(generic.ListView):
    model = models.PlanAnual
    form_class = forms.PlanAnualForm


class PlanAnualCreateView(generic.CreateView):
    model = models.PlanAnual
    form_class = forms.PlanAnualForm


class PlanAnualDetailView(generic.DetailView):
    model = models.PlanAnual
    form_class = forms.PlanAnualForm


class PlanAnualUpdateView(generic.UpdateView):
    model = models.PlanAnual
    form_class = forms.PlanAnualForm
    pk_url_kwarg = "pk"


class BaseListView(generic.ListView):
    model = models.Base
    form_class = forms.BaseForm


class BaseCreateView(generic.CreateView):
    model = models.Base
    form_class = forms.BaseForm


class BaseDetailView(generic.DetailView):
    model = models.Base
    form_class = forms.BaseForm


class BaseUpdateView(generic.UpdateView):
    model = models.Base
    form_class = forms.BaseForm
    pk_url_kwarg = "pk"
