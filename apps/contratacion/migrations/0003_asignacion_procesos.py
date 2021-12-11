from django.db import migrations
import itertools
import random


class Migration(migrations.Migration):
    dependencies = [
        ('contratacion', '0002_auto_20210304_1814'),
    ]

    def remove_duplicated_records(model, fields):
        from apps.contratacion.models import Proceso
        from apps.autenticacion.models import USUARIO

        procesos = Proceso.objects.prefetch_related('usuarios', 'usuarios__usuario', 'usuarios__usuario__estado').all()

        # [x.nombre for x in procesos[0].usuarios.all()[0].estado.all()]
        procesos_to_save = []
        for proc in procesos:
            try:
                for usuario in proc.usuarios.all():
                    estados = [estado.nombre for estado in [estado for estado in usuario.estado.all()]]
                    if proc.estado.nombre in estados:
                        proc.usuario = usuario
                    else:
                        usuarios = USUARIO.objects.filter(estado__nombre=proc.estado.nombre)
                        proc.usuario = random.choice(usuarios)
                        print(f'falta asigacion proceso {proc.id} - - ')

                procesos_to_save.append(
                    proc
                )
            except Exception as e:
                print(f'Error {e.__str__()} con proceso {proc.id} - pro: {proc}')
        Proceso.objects.bulk_update(procesos_to_save, ['usuario'])

    operations = [
        migrations.RunPython(remove_duplicated_records),
    ]
