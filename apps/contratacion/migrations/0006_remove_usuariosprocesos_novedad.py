# Generated by Django 2.2.24 on 2021-06-20 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contratacion', '0005_usuariosprocesos_novedad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuariosprocesos',
            name='novedad',
        ),
    ]
