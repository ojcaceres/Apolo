# Generated by Django 2.2.24 on 2021-09-07 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratacion', '0015_auto_20210905_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='modificacion',
            name='cdp',
            field=models.CharField(blank=True, default=None, max_length=16, null=True),
        ),
    ]
