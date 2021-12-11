from enum import Enum

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


from apps.autenticacion.models import USUARIO, Modulos
from apps.estructura.models import Estado, Dependencia, Proyecto, TipologiaEspecifica


class ProcesoEstados(Enum):
    CREACION_RH = "CREACION_RH"
    REVISION = "REVISION"
    REVISIONMOD = "REVISIONMOD"
    DEVUELTO_RADICADO = "DEVUELTO_RADICADO"
    DEVUELTO_ALISTAMIENTO = "DEVUELTO_ALISTAMIENTO"
    REVISAR = "REVISAR"
    REVISARMOD = "REVISARMOD"
    SUBSANACION = "SUBSANACION"
    PRIMER_FLUJO = "PRIMER_FLUJO"
    NUMERACION_CONTRATO = "NUMERACION_CONTRATO"
    SECOP_PUBLICACION = "SECOP_PUBLICACION"
    SECOP_REVISAR = "SECOP_REVISAR"
    SEGUNDO_FLUJO = "SEGUNDO_FLUJO"
    FLUJO_APROBACION = "FLUJO_APROBACION"
    SECOP_FIRMA = "SECOP_FIRMA"
    FIRMADO = "FIRMADO"
    SOLICITUD_CRP = "SOLICITUD_CRP"
    TRAMITE_FINANCIERA = "TRAMITE_FINANCIERA"
    CRP_TRAMITADO = "CRP_TRAMITADO"
    CRP_DEVUELTO = "CRP_DEVUELTO"
    PERFECCIONAMIENTO = 'PERFECCIONAMIENTO'
    FINALIZADO = "FINALIZADO"
    RECHAZADO = 'RECHAZADO'
    EJECUCION = "EJECUCION"
    SUSPENSION = "SUSPENSION"



    def get_modulo(self):
        if self.name in [self.CREACION_RH.value]:
            return Modulos.CREACION

        if self.name in [self.REVISION.value, self.REVISIONMOD.value, self.DEVUELTO_RADICADO.value]:
            return Modulos.RADICACION

        if self.name in [self.SUBSANACION.value,
                         self.DEVUELTO_ALISTAMIENTO.value,
                         self.REVISAR.value,
                         self.PRIMER_FLUJO.value,
                         ]:
            return Modulos.ALISTAMIENTO

        if self.name in [self.NUMERACION_CONTRATO.value, ]:
            return Modulos.NUMERACION

        if self.name in [self.SECOP_PUBLICACION.value]:
            return Modulos.SECOP_PUBLICAR

        if self.name in [self.SECOP_REVISAR.value, self.SEGUNDO_FLUJO.value, self.SECOP_FIRMA]:
            return Modulos.SECOP_FLUJOS

        if self.name in [self.FIRMADO.value, self.SOLICITUD_CRP.value, self.CRP_DEVUELTO.value]:
            return Modulos.TRAMITE_CRP

        if self.name in [self.TRAMITE_FINANCIERA.value]:
            return Modulos.FINANCIERA

        if self.name in [self.PERFECCIONAMIENTO.value]:
            return Modulos.PERFECCIONAMIENTO

        if self.name in [self.RECHAZADO.value, self.FINALIZADO.value, self.EJECUCION.value, self.SUSPENSION.value]:
            return Modulos.CONTROL

    def is_same_modulo(self):
        pass

    def __str__(self):
        return self.value




class Modificacion(models.Model):

    class Meta:
        verbose_name_plural = "Modificaciones"

    CHOICES = (
    ('CONTRATO INICIAL', 'CONTRATO_INICIAL'),
    ('OTROSI' , 'OTROSI'),
    ('ADICION' , 'ADICION'),
    ('CESION' , 'CESION'),
    ('PRORROGA' , 'PRORROGA'),
    ('SUSPENSION' , 'SUSPENSION'),
    ('REINICIO' , 'REINICIO'),
    ('ADICION_PRORROGA' , 'ADICION_PRORROGA'),
    ('ADICION_PRORROGA_OTROSI', 'ADICION_PRORROGA_OTROSI'),
    ('ADICION_PRORROGA_SUSPENSION','ADICION_PRORROGA_SUSPENSION'),
    ('TERMINACION_ANTICIPADA' , 'TERMINACION_ANTICIPADA')
    )
    
    modificacion = models.CharField(max_length=300, choices = CHOICES, default='CONTRATO_INICIAL')
    numero_contrato = models.CharField(null=True, blank=True, default=None, max_length=16)
    vigencia = models.CharField(max_length=8, null=True, default=None, blank=True)
    duracion = models.CharField(null=True, blank=True, default=None, max_length=16)
    fecha_firma_modificacion = models.DateTimeField(null=True, blank=True, default=None)
    fechaInicio = models.DateTimeField(null=True, blank=True, default=None)
    fechaFin = models.DateTimeField(null=True, blank=True, default=None)
    fechaReinicio = models.DateTimeField(null=True, blank=True, default=None)
    cdp = models.CharField(null=True, blank=True, default=None, max_length=16)
    valor = models.CharField(null=True, blank=True, default=None, max_length=16)
    documentoCedente = models.CharField(null=True, blank=True, default=None, max_length=16)
    cedente = models.CharField(null=True, blank=True, default=None, max_length=255)
    documentoCesionario = models.CharField(null=True, blank=True, default=None, max_length=16)
    cesionario = models.CharField(null=True, blank=True, default=None, max_length=255)
    
    def __str__(self):
        return f'{self.modificacion} - {self.numero_contrato} - {self.vigencia}'

class Proceso(models.Model):
    usuarios = models.ManyToManyField(USUARIO, through='UsuariosProcesos')
    modificaciones = models.ManyToManyField(Modificacion,  through='ModificacionesProcesos', related_name='Modificaciones')
    modificacion= models.CharField(max_length=30, null=True, blank=True, default="CONTRATO_INICIAL")
    link = models.URLField(null=True, blank=True, default=None)

    # Radicacion
    id_cupo = models.CharField(max_length=16, null=True, blank=True, default="")
    numero_de_proceso = models.CharField(null=True, blank=True, default=None, max_length=20)
    dependencia_contratista = models.ForeignKey(Dependencia, on_delete=models.CASCADE, null=True, blank=True,
                                                default=None)
    nombre_contratista = models.CharField(max_length=128, null=True, blank=True, default=None)
    cedula_contratista = models.CharField(max_length=12, null=True, blank=True, default=None)

    fecha_radicacion = models.DateTimeField(auto_created=True, auto_now_add=True, editable=False)

    # CSV
    plazo = models.CharField(null=True, blank=True, default=None, max_length=16)
    numero_cdp = models.CharField(null=True, blank=True, default=None, max_length=16)
    valor_cdp = models.CharField(null=True, blank=True, default=None, max_length=16)
    valor_contrato = models.CharField(null=True, blank=True, default=None, max_length=16)

    numero_contrato = models.CharField(null=True, blank=True, default=None, max_length=16)
    vigencia = models.CharField(max_length=8, null=True, default=None, blank=True)

    # Estados
    usuario = models.ForeignKey(USUARIO, on_delete=models.CASCADE, null=True, default=None, related_name="usuario")

    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, to_field='nombre', default=ProcesoEstados.REVISION)

    devuelto = models.BooleanField(default=False)
    estado_devolucion = models.ForeignKey(Estado, on_delete=models.CASCADE, to_field='nombre', null=True, blank=True, default=None,related_name="estado_devolucion")

    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, null=True, blank=True, default=None)
    tipologia_especifica = models.ForeignKey(TipologiaEspecifica,
                                             on_delete=models.CASCADE,
                                             null=True,
                                             blank=True,
                                             default=None)

    objeto = models.TextField(null=True, blank=True, default=None, max_length=2048)
    numero_crp = models.CharField(null=True, blank=True, default=None, max_length=16)
    valor_crp = models.CharField(null=True, blank=True, default=None, max_length=16)

    nombre_supervisor = models.CharField(null=True, blank=True, default=None, max_length=120)
    ultima_actualizacion = models.DateTimeField(auto_now=True, editable=False)
    caso_seven = models.CharField(max_length=20, null=True, default=None, blank=True)

    fecha_inicio = models.DateField(null=True, default=None, blank=True)
    fecha_final = models.DateField(null=True, default=None, blank=True)

    class Meta:
        ordering = ['fecha_radicacion']


 #    @property
 #   def get_modificacion(self):
 #        return [x.modificacion for x in self.modificaciones.all()]


    def is_devuelto(self, old):
        actual = [str(x) for x in [ProcesoEstados.DEVUELTO_ALISTAMIENTO,
                                   ProcesoEstados.DEVUELTO_RADICADO,
                                   ProcesoEstados.CRP_DEVUELTO]
                  if str(x) == str(self.estado)]

        viejo = [str(x) for x in [ProcesoEstados.DEVUELTO_ALISTAMIENTO,
                                  ProcesoEstados.DEVUELTO_RADICADO,
                                  ProcesoEstados.CRP_DEVUELTO]
                 if str(x) == str(old.estado)]

        return actual and not viejo

    def save(self, *args, **kw):
        old = type(self).objects.get(pk=self.pk) if self.pk else None

        if old and not old.devuelto:
            if self.is_devuelto(old):
                self.devuelto = True
        super(Proceso, self).save(*args, **kw)

    def __str__(self):
        return f'{str(self.id)} - {str(self.numero_de_proceso)}'  # str(self.numero_contrato)


@receiver(pre_save, sender=Proceso)
def my_callback(sender, instance, *args, **kwargs):
    # todo obtener el ID, y obteneri nstancia, si se está agregando el numero de contrato, validar que ningún otro lo tenga.
    pass



class UsuariosProcesos(models.Model):
    class Meta:
        verbose_name = "Asignacion Usuario-Procesos"
        verbose_name_plural = "Asignaciones de usuarios y procesos"
        ordering = ('-date',)

    proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE)
    usuario = models.ForeignKey(USUARIO, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, default=1)
    novedad = models.CharField(max_length=300, null=True, blank=True)
    date = models.DateTimeField(auto_created=True, auto_now_add=True)

    def nombre_usuario(self):
        return self.usuario.get_full_name()

    def modulo(self):
        return self.estado.modulo.nombre

    def __str__(self):
        return f'{self.proceso} - {self.usuario}'

class ModificacionesProcesos(models.Model):
    class Meta:
        verbose_name = "Asignacion Modificaciones-Procesos"
        verbose_name_plural = "Asignaciones de Modificaciones y procesos"
   
    modificacion = models.ForeignKey(Modificacion, on_delete=models.CASCADE)
    proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE, null=True, default=None)
    
    def __str__(self):
        return f'{self.modificacion}'


class Importar(models.Model):
    nombre = models.CharField(max_length=64)
    date = models.DateTimeField(auto_now_add=True, auto_created=True)
    tipo = models.CharField(max_length=32)
    logs = models.TextField(default=None, null=True, blank=True)

    def __str__(self):
        return self.nombre