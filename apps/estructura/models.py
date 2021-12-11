from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse



class PlanDeDesarrollo(models.Model):
    class Meta:
        verbose_name = 'Plan De Desarrollo'
        verbose_name_plural = 'Planes De Desarrollo'


    nombre = models.CharField(max_length=240)

    def __str__(self):
        return f'{self.nombre}'

    def get_absolute_url(self):
        return reverse("estructura_pdd_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("estructura_pdd_update", args=(self.pk,))


class Proyecto(models.Model):
    nombre = models.CharField(max_length=240)
    numero = models.CharField(max_length=10, primary_key=True)
    plan_de_desarrollo = models.ForeignKey(PlanDeDesarrollo, on_delete=models.CASCADE, default=None, null=True, blank=True)


    def __str__(self):
        return f'{self.nombre}'

    def get_absolute_url(self):
        return reverse("estructura_proyecto_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("estructura_proyecto_update", args=(self.pk,))


class Modulo(models.Model):
    nombre = models.CharField(max_length=120)

    class Meta:
        pass

    def __str__(self):
        return str(self.nombre)

    def get_absolute_url(self):
        return reverse("estructura_modulo_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("estructura_modulo_update", args=(self.pk,))


class Estado(models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    modulo = models.ForeignKey(Modulo, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        pass

    def __str__(self):
        return str(self.nombre)

    def is_same_modulo(self, modulo):
        return self.nombre == modulo

    def get_absolute_url(self):
        return reverse("estructura_estado_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("estructura_estado_update", args=(self.pk,))


class Dependencia(models.Model):
    # Fields
    nombre = models.CharField(max_length=120)

    class Meta:
        pass

    def __str__(self):
        return str(self.nombre)

    def get_absolute_url(self):
        return reverse("estructura_dependencia_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("estructura_dependencia_update", args=(self.pk,))


class TipologiaEspecifica(models.Model):
    nombre = models.CharField(max_length=120)

    class Meta:
        verbose_name = "Tipología específica"
        verbose_name_plural = "Tipologías específicas"

    def __str__(self):
        return str(self.nombre)

    def get_absolute_url(self):
        return reverse("estructura_tipologia_especifica_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("estructura_tipologia_especifica_update", args=(self.pk,))



