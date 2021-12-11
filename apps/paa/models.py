from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class PlanAnual(models.Model):
    class Meta:
        verbose_name = 'Plan Anual'
        verbose_name_plural = 'Planes Anuales' 

    estadodelcupo= models.CharField(max_length=240)
    nombreplan= models.CharField(max_length=240)
    vigencia= models.BigIntegerField(null=True)
    proyecto= models.BigIntegerField(null=True)
    nombreproyecto= models.CharField(max_length=240)
    fuentedefinanciacion= models.CharField(max_length=240)
    códigofuentefinanciación= models.BigIntegerField(null=True)
    componentegasto= models.BigIntegerField(null=True)
    códigodecomponentegasto= models.CharField(max_length=240)
    unidadoperativa= models.BigIntegerField(null=True)
    descripcióncentrodecosto= models.CharField(max_length=240)
    localidad= models.BigIntegerField(null=True)
    códigorubropresupuestal= models.CharField(max_length=240)
    nombrerubroprespupuestal= models.TextField()
    pmrcodigo= models.BigIntegerField(null=True)
    pmrnombre= models.CharField(max_length=240)
    metacodigo= models.BigIntegerField(null=True)
    nombredelameta= models.TextField()
    codigoactividad= models.BigIntegerField(null=True)
    nombreactividad= models.CharField(max_length=240)
    códigodelservicio= models.BigIntegerField(null=True)
    nombreservicio= models.CharField(max_length=240)
    descripcioncupo= models.CharField(max_length=240)
    idcupo= models.BigIntegerField(null=True)
    fechaestimadaproceso= models.DateTimeField(auto_created=True, editable=False, null=True)
    fechaestimadacompra= models.DateTimeField(auto_created=True, editable=False, null=True)
    fechaestimadapago= models.DateTimeField(auto_created=True, editable=False, null=True)
    fecha_radicacion= models.DateTimeField(auto_created=True, editable=False, null=True)
    plazo= models.BigIntegerField(null=True)
    presupuestoprogramado= models.BigIntegerField(null=True)
    modificaciones = models.BigIntegerField(null=True)
    ejecucion = models.BigIntegerField(null=True)
    presupuestovigente = models.BigIntegerField(null=True)
    cupoconvigenciafutura = models.CharField(max_length=240)
    descripcionobjeto= models.TextField()
    modalidaddeadquisición = models.BigIntegerField(null=True)
    nombremodalidadadquisicion= models.CharField(max_length=240)
    modalidaddeseleccion = models.BigIntegerField(null=True)
    nombremodalidadseleccion= models.CharField(max_length=240)
    tipodecontratacion = models.BigIntegerField(null=True)
    nombretipodecontratacion= models.CharField(max_length=240)
    individualconjunta= models.CharField(max_length=240)
    dependencia = models.BigIntegerField(null=True)
    nombredependencia= models.CharField(max_length=240) 
    unspc = models.BigIntegerField(null=True)
    numerocdp = models.BigIntegerField(null=True)
    valorcdp = models.BigIntegerField(null=True)
    fechadesolicituddecdp= models.DateTimeField(auto_created=True, editable=False, null=True)
    fechadecdp= models.DateTimeField(auto_created=True, editable=False, null=True)
    saldodecupodespuesdecdp = models.BigIntegerField(null=True)
    númerodecontrato = models.BigIntegerField(null=True)
    objetodelcontrato = models.TextField()
    númerodelcrp = models.BigIntegerField(null=True)
    valordelcrp = models.BigIntegerField(null=True)
    saldodedisponibilidadesporcomprometer = models.BigIntegerField(null=True)
    compromisosconautorizacióndegiros = models.BigIntegerField(null=True)
    fechadegiros= models.DateTimeField(auto_created=True, editable=False, null=True)
    compromisossinautorizacion = models.BigIntegerField(null=True)
    númerodecaso = models.BigIntegerField(null=True)
    historicocaso= models.CharField(max_length=240)

    def __str__(self):
        return f'{self.nombre}'

    def get_absolute_url(self):
        return reverse("estructura_pdd_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("estructura_pdd_update", args=(self.pk,))

class Base(models.Model):

    numero_contrato = models.BigIntegerField(null=True)
    proceso_selección = models.BigIntegerField(null=True)
    tipologia = models.CharField(max_length=240)
    modalidad = models.CharField(max_length=240)
    fechasuscripcion = models.DateTimeField(
        auto_created=True, editable=False)
    fechainicial = models.DateTimeField(auto_created=True, editable=False)
    fechafinal = models.DateTimeField(auto_created=True, editable=False)
    plazo = models.BigIntegerField(null=True)
    idcupo = models.BigIntegerField(null=True)
    numerocdp = models.BigIntegerField(null=True)
    numerocrp = models.BigIntegerField(null=True)
    idcupoaju = models.BigIntegerField(null=True)
    fecharegistro = models.DateTimeField(
        auto_created=True,  editable=False)
    objeto = models.TextField()
    fuente = models.CharField(max_length=240)
    proyecto = models.CharField(max_length=240)
    tipoidcontratista = models.CharField(max_length=10)
    numeroid = models.BigIntegerField(null=True)
    nombrecontratista = models.CharField(max_length=240)
    idsupervisor = models.BigIntegerField(null=True)
    nombresupervisor = models.CharField(max_length=240)
    valorcrp = models.BigIntegerField(null=True)
    anulaciones = models.BigIntegerField(null=True)
    valorneto = models.BigIntegerField(null=True)
    valorcontrato = models.BigIntegerField(null=True)

def __str__(self):
    return f'{self.numerocdp}'

def get_absolute_url(self):
    return reverse("estructura_proyecto_detail", args=(self.pk,))

def get_update_url(self):
    return reverse("estructura_proyecto_update", args=(self.pk,))
