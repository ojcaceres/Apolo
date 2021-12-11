from django import forms
from django.core.exceptions import ValidationError

from apps.estructura.models import Estado
from .models import Proceso, ProcesoEstados


class CreateProcesoRadicacionForm(forms.ModelForm):

    def save(self, commit=True):
        
        proceso = super(CreateProcesoRadicacionForm, self).save(commit=False)
        proceso.estado = Estado.objects.get(nombre=ProcesoEstados.REVISION)
        return proceso

    def __init__(self, *args, **kwargs):
        super(CreateProcesoRadicacionForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(CreateProcesoRadicacionForm, self).clean()
        cleaned_data.get('dependencia_contratista')

    class Meta:
        model = Proceso
        fields = [
            "id_cupo",
            "numero_de_proceso",
            "dependencia_contratista",
            "nombre_contratista",
            "cedula_contratista",
        ]
        widgets = {
            "id_cupo": forms.TextInput(
                attrs={'class': 'form-control col-sm-10',
                       'autocomplete': 'false'}
            ),
            "numero_de_proceso": forms.TextInput(
                attrs={'class': 'form-control col-sm-10',
                       'autocomplete': 'false'}
            ),
            "nombre_contratista": forms.TextInput(
                attrs={'class': 'form-control col-sm-10',
                       'autocomplete': 'false'}
            ),
            "cedula_contratista": forms.TextInput(
                attrs={'class': 'form-control col-sm-10',
                       'autocomplete': 'false'}
            ),
        }


class ProcesoGeneralForm(forms.ModelForm):
    pk = None
    check_numero_proceso = True
    editable_fields = []

    def __init__(self,  *args, **kwargs):
        instance = kwargs.get('instance', None)
        super(ProcesoGeneralForm, self).__init__(*args, **kwargs)
        if instance:
            self.pk = instance.pk
            print(self.pk)
            for key in self.fields.keys():
                if getattr(instance, key) in (None, ''):
                    self.fields[key].widget.attrs['readonly'] = False
                else:
                    self.fields[key].widget.attrs['readonly'] = True

    def custom_clean(self, custom_clean):
        pass

    def clean(self, *args, **kwargs):
        cleaned_data = super(ProcesoGeneralForm, self).clean()
        self.custom_clean(cleaned_data)

        cleaned_data.get("tipologia_especifica")
        cleaned_data.get('estado_novedad')

        cleaned_data.get('dependencia_contratista')
        cleaned_data.get('proyecto')
        cleaned_data.get('estado')
        cleaned_data.get('novedad')

        if cleaned_data.get('numero_de_proceso') is None and self.check_numero_proceso:
            raise ValidationError(
                "No se puede pasar a una siguiente fase si el número de proceso es nulo")

    class Meta:
        model = Proceso
        fields = "__all__"
        exclude = ['usuarios', 'usuario','modificaciones', 'devuelto','estado_devolucion']
        widgets = {
            "devuelto": forms.CheckboxInput(attrs={'disabled': 'disabled'}),
            "modificacion": forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autocomplete': 'false'}),
            "link": forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autocomplete': 'false'}),
            "id_cupo": forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autocomplete': 'false'}),
            "caso_seven": forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autocomplete': 'false'}),
            "valor_contrato": forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autocomplete': 'false'}),
            "numero_contrato": forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autocomplete': 'false'}),
            "vigencia": forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autocomplete': 'false'}),
            "plazo": forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autocomplete': 'false'}),
            "estado": forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autocomplete': 'false'}),
            "proyecto": forms.Select(attrs={'class': 'form-control col-sm-10', 'autocomplete': 'false'}),
            "tipologia_especifica": forms.Select(attrs={'class': 'form-control col-sm-10', 'autocomplete': 'false'}),
            "objeto": forms.Textarea(attrs={'class': 'form-control col-sm-10', 'rows': '3', 'autocomplete': 'false'}),
            "numero_crp": forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autocomplete': 'false'}),
            "numero_cdp": forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autocomplete': 'false'}),
            "numero_de_proceso": forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autocomplete': 'false'}),
            "dependencia_contratista": forms.Select(attrs={'class': 'form-control col-sm-10', 'autocomplete': 'false'}),
            "valor_cdp": forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autocomplete': 'false'}),
            "cedula_contratista": forms.TextInput(
                attrs={'class': 'form-control col-sm-10', 'autocomplete': 'false'}),
            "numero_caso": forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autocomplete': 'false'}),
            "nombre_contratista": forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autocomplete': 'false'}),
            "nombre_supervisor": forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autocomplete': 'false'}),
            "valor_crp": forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autocomplete': 'false'}),
            "fecha_inicio": forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autocomplete': 'false'}),
            "fecha_final": forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autocomplete': 'false'}),
           
        }

class ProcesoAlistamientoForm(ProcesoGeneralForm):
    editable_fields = ['link']


class NumeracionForm(ProcesoGeneralForm):
    editable_fields = ['numero_contrato','vigencia']

    def custom_clean(self, cleaned):
        if cleaned.get('numero_contrato', None) == None or cleaned.get('vigencia', None) == None :
            raise ValidationError('el Número de contrato y Vigencias no pueden estar vacíos')
        if Proceso.objects.exclude(id=self.pk) \
                .filter(
            numero_contrato=cleaned.get('numero_contrato')
        ).exists():
            raise ValidationError(
                'Otro Proceso ya tiene este número de contrato')



class TramiteCRPForm(ProcesoGeneralForm):
    editable_fields = ['numero_crp', 'numero_cdp']

class RadicacionForm(ProcesoGeneralForm):
    check_numero_proceso = False
    editable_fields = ['nombre_contratista']




