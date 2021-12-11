import os
from django.db import migrations

from apps.autenticacion.models import Modulos


class Migration(migrations.Migration):
    dependencies = [
        ("estructura", "0001_initial")
    ]

    def load_initial_data_dependencia(apps, schema_editor):
        Dependencia = apps.get_model('estructura', 'Dependencia')

        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(dir_path, "files", "dependencias.txt")

        data_file = open(file_path, encoding="utf8")
        dependencias = []
        for line in data_file.readlines():
            line_info = line.replace("\n", "")
            dependencias.append(
                Dependencia(
                    nombre=line_info.strip()
                )
            )

        Dependencia.objects.bulk_create(dependencias)

    def load_initial_data_estados(apps, schema_editor):
        Estado = apps.get_model('estructura', 'Estado')
        Modulo = apps.get_model('estructura', 'Modulo')

        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(dir_path, "files", "estados.txt")

        data_file = open(file_path, encoding="utf8")
        estados = []

        for line in data_file.readlines():
            estado, modulo = line.strip().split(",")
            modulo = Modulo.objects.get(nombre=modulo)
            estados.append(
                Estado(
                    nombre=estado,
                    modulo=modulo
                )
            )

        Estado.objects.bulk_create(estados)

    def load_initial_data_modulos(apps, schema_editor):
        Modulo = apps.get_model('estructura', 'Modulo')

        listado = []
        for line in Modulos.list():
            listado.append(
                Modulo(
                    nombre=line
                )
            )

        Modulo.objects.bulk_create(listado)

    def load_initial_data_tipologias(apps, schema_editor):
        TipologiaEspecifica = apps.get_model('estructura', 'TipologiaEspecifica')

        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(dir_path, "files", "tipologias_especificas.txt")

        data_file = open(file_path, encoding="utf8")
        listado = []
        for line in data_file.readlines():
            line_info = line.replace("\n", "")
            listado.append(
                TipologiaEspecifica(
                    nombre=line_info.strip()
                )
            )

        TipologiaEspecifica.objects.bulk_create(listado)

    def load_initial_data_proyecto(apps, schema_editor):
        Proyecto = apps.get_model('estructura', 'Proyecto')

        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(dir_path, "files", "proyecto.txt")

        data_file = open(file_path, encoding="utf8")
        listado = []
        for line in data_file.readlines():
            line_info = line.replace("\n", "").split(';')
            listado.append(
                Proyecto(
                    nombre=line_info[1].strip(),
                    numero=line_info[0].strip()
                )
            )

        Proyecto.objects.bulk_create(listado)

    operations = [
        migrations.RunPython(load_initial_data_dependencia),
        migrations.RunPython(load_initial_data_modulos),
        migrations.RunPython(load_initial_data_estados),
        migrations.RunPython(load_initial_data_tipologias),
        migrations.RunPython(load_initial_data_proyecto),
    ]
