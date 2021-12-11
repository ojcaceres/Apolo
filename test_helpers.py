import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from datetime import datetime

from estructura import models as estructura_models
from contratacion import models as contratacion_models


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_User(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_AbstractUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractUser.objects.create(**defaults)


def create_AbstractBaseUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractBaseUser.objects.create(**defaults)


def create_Group(**kwargs):
    defaults = {
        "name": "%s_group" % random_string(5),
    }
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_ContentType(**kwargs):
    defaults = {
    }
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_estructura_proyecto(**kwargs):
    defaults = {}
    defaults["nombre"] = ""
    defaults["numero"] = ""
    defaults.update(**kwargs)
    return estructura_models.proyecto.objects.create(**defaults)
def create_estructura_modulo(**kwargs):
    defaults = {}
    defaults["nombre"] = ""
    defaults["numero"] = ""
    defaults.update(**kwargs)
    return estructura_models.modulo.objects.create(**defaults)
def create_estructura_estado(**kwargs):
    defaults = {}
    defaults["nombre"] = ""
    defaults["numero"] = ""
    defaults.update(**kwargs)
    return estructura_models.estado.objects.create(**defaults)
def create_estructura_estado_novedad(**kwargs):
    defaults = {}
    defaults["novedad"] = ""
    if "estado" not in kwargs:
        defaults["estado"] = create_estructura_estado()
    defaults.update(**kwargs)
    return estructura_models.estado_novedad.objects.create(**defaults)
def create_estructura_dependencia(**kwargs):
    defaults = {}
    defaults["nombre"] = ""
    defaults["numero"] = ""
    defaults.update(**kwargs)
    return estructura_models.dependencia.objects.create(**defaults)
def create_estructura_tipologia_especifica(**kwargs):
    defaults = {}
    defaults["nombre"] = ""
    defaults["numero"] = ""
    defaults.update(**kwargs)
    return estructura_models.tipologia_especifica.objects.create(**defaults)
def create_estructura_usuario_apolo(**kwargs):
    defaults = {}
    defaults["numero"] = ""
    if "dependencia" not in kwargs:
        defaults["dependencia"] = create_estructura_dependencia()
    if "modulo" not in kwargs:
        defaults["modulo"] = create_estructura_modulo()
    if "usuario" not in kwargs:
        defaults["usuario"] = create_User()
    defaults.update(**kwargs)
    return estructura_models.usuario_apolo.objects.create(**defaults)
def create_contratacion_proceso(**kwargs):
    defaults = {}
    defaults["numero_de_contrato"] = ""
    defaults["objeto"] = ""
    defaults["numero_crp"] = ""
    defaults["numero_cdp"] = ""
    defaults["numero_de_proceso"] = ""
    defaults["valor_cdp"] = ""
    defaults["fecha_terminacion_con_adicion"] = datetime.now()
    defaults["documento_de_identidad"] = ""
    defaults["numero_caso"] = ""
    defaults["nombre_contratista"] = ""
    defaults["nombre_supervisor"] = ""
    defaults["valor_crp"] = ""
    if "usuarios" not in kwargs:
        defaults["usuarios"] = create_estructura_usuario_apolo()
    if "estado_novedad" not in kwargs:
        defaults["estado_novedad"] = create_estructura_estado_novedad()
    if "dependencia_contratista" not in kwargs:
        defaults["dependencia_contratista"] = create_estructura_dependencia()
    if "proyecto" not in kwargs:
        defaults["proyecto"] = create_estructura_proyecto()
    if "tipologia_especifica" not in kwargs:
        defaults["tipologia_especifica"] = create_estructura_tipologia_especifica()
    defaults.update(**kwargs)
    return contratacion_models.Proceso.objects.create(**defaults)
