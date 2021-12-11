from django import forms
from . import models


class proyectoForm(forms.ModelForm):
    class Meta:
        model = models.Proyecto
        fields = [
            "nombre",
        ]


class moduloForm(forms.ModelForm):
    class Meta:
        model = models.Modulo
        fields = [
            "nombre",
        ]


class estadoForm(forms.ModelForm):
    class Meta:
        model = models.Estado
        fields = [
            "nombre",
        ]

class dependenciaForm(forms.ModelForm):
    class Meta:
        model = models.Dependencia
        fields = [
            "nombre",
        ]


class tipologia_especificaForm(forms.ModelForm):
    class Meta:
        model = models.TipologiaEspecifica
        fields = [
            "nombre",
        ]
