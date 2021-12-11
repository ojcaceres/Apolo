from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.db.models import Max, Count


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('estructura', '0002_load_initial_data'),
        ('contratacion', '0001_initial'),
    ]

    def remove_duplicated_records(model, fields):
        from apps.contratacion.models import UsuariosProcesos

        unique_fields = ['proceso', 'usuario']

        duplicates = (
            UsuariosProcesos.objects.values(*unique_fields)
                .order_by()
                .annotate(max_id=Max('id'), count_id=Count('id'))
                .filter(count_id__gt=1)
        )

        for duplicate in duplicates:
            (
                UsuariosProcesos.objects
                    .filter(**{x: duplicate[x] for x in unique_fields})
                    .exclude(id=duplicate['max_id'])
                    .delete()
            )

    operations = [
        migrations.AddField(
            model_name='proceso',
            name='usuario',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='usuario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RunPython(remove_duplicated_records),
        migrations.AlterUniqueTogether(
            name='usuariosprocesos',
            unique_together={('proceso', 'usuario', 'estado')},
        ),
    ]
