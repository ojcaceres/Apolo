# Generated by Django 2.2.2 on 2021-02-16 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dependencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('nombre', models.CharField(max_length=240)),
                ('numero', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='TipologiaEspecifica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
            ],
            options={
                'verbose_name': 'Tipología específica',
                'verbose_name_plural': 'Tipologías específicas',
            },
        ),
        migrations.CreateModel(
            name='ValidacionEstado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('validacion', models.CharField(max_length=64)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estructura.Estado')),
            ],
            options={
                'verbose_name': 'Validación de estado',
                'verbose_name_plural': 'Validaciones de estados',
            },
        ),
        migrations.AddField(
            model_name='estado',
            name='modulo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='estructura.Modulo'),
        ),
    ]
