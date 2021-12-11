from django import forms


class RevisarProcesoForm(forms.Form):
    cedula = forms.CharField(label = "Cédula ")
