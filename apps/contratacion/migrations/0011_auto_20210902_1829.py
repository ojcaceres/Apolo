# Generated by Django 2.2.24 on 2021-09-02 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contratacion', '0010_auto_20210806_1217'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modificacion', models.CharField(choices=[('PRIMERA_CONTRATACION', 'PRIMERA_CONTRATACION'), ('OTROSI', 'OTROSI'), ('ADICION', 'ADICION'), ('CESION', 'CESION'), ('PRORROGA', 'PRORROGA'), ('SUSPENSION', 'SUSPENSION'), ('REINICIO', 'REINICIO'), ('ADICION_PRORROGA', 'ADICION_PRORROGA'), ('TERMINACION_ANTICIPADA', 'TERMINACION_ANTICIPADA')], default='PRIMERA_CONTRATACION', max_length=300)),
                ('numero_contrato', models.CharField(blank=True, default=None, max_length=16, null=True)),
                ('vigencia', models.CharField(blank=True, default=None, max_length=8, null=True)),
                ('duracion', models.CharField(blank=True, default=None, max_length=16, null=True)),
                ('fecha_firma_modificacion', models.DateTimeField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name_plural': 'Modificaciones',
            },
        ),
        migrations.CreateModel(
            name='ProcesoRaiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_radicacion', models.DateTimeField(auto_created=True, auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ModificacionesProcesos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contratacion.Modificacion')),
                ('proceso', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='contratacion.Proceso')),
            ],
            options={
                'verbose_name': 'Asignacion Modificaciones-Procesos',
                'verbose_name_plural': 'Asignaciones de Modificaciones y procesos',
            },
        ),
        migrations.AddField(
            model_name='proceso',
            name='modificaciones',
            field=models.ManyToManyField(related_name='Modificaciones', through='contratacion.ModificacionesProcesos', to='contratacion.Modificacion'),
        ),
        migrations.AddField(
            model_name='proceso',
            name='procesoraiz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contratacion.ProcesoRaiz'),
        ),
    ]
