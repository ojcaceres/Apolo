# Generated by Django 2.2.24 on 2021-08-06 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contratacion', '0009_auto_20210702_0912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='validacionestadoproceso',
            name='proceso',
        ),
        migrations.RemoveField(
            model_name='validacionestadoproceso',
            name='validacion_estado',
        ),
        migrations.RemoveField(
            model_name='proceso',
            name='validaciones',
        ),
        migrations.DeleteModel(
            name='EstadoNovedad',
        ),
        migrations.DeleteModel(
            name='ValidacionEstadoProceso',
        ),
    ]
