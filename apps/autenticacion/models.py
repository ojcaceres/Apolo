from enum import Enum
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.estructura.models import Dependencia, Modulo, Estado


class Modulos(Enum):
    CREACION = "CREACION"
    RADICACION = 'RADICACION'
    ALISTAMIENTO = 'ALISTAMIENTO'
    NUMERACION = 'NUMERACION'
    SECOP_PUBLICAR = 'SECOP_PUBLICAR'
    SECOP_FLUJOS = 'SECOP_FLUJOS'
    TRAMITE_CRP = 'TRAMITE_CRP'
    FINANCIERA = 'FINANCIERA'
    PERFECCIONAMIENTO = 'PERFECCIONAMIENTO'
    CONTROL = 'CONTROL'

    def __str__(self):
        return self.value

    @staticmethod
    def list():
        return list(map(lambda g: g.value, Modulos))


class EstadosDeUsuarios(models.Model):
    class Meta:
        verbose_name = 'Estado de usuarios'
        verbose_name_plural = 'Estados de usuarios'

    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, default=None, null=True, blank=True)
    usuario = models.ForeignKey('USUARIO', on_delete=models.CASCADE, default=None, null=True, blank=True)


class USUARIO(AbstractUser):
    first_name = models.CharField(_('first name'), max_length=100, blank=True)
    dependencia = models.ForeignKey(Dependencia, on_delete=models.CASCADE, default=None, null=True, blank=True)
    estado = models.ManyToManyField(Estado, blank=True,
                                    through=EstadosDeUsuarios)

    class Meta:
        verbose_name_plural = "USUARIOS"
