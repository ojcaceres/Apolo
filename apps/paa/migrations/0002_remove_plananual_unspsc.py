# Generated by Django 2.2.24 on 2021-08-27 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paa', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plananual',
            name='unspsc',
        ),
    ]
