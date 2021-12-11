from django.shortcuts import render
from apps.contratacion.models import Proceso
from django.views.decorators.csrf import csrf_exempt
from .forms import RevisarProcesoForm


@csrf_exempt
def RevisarProceso(request):
    if request.method == 'POST':
        form = RevisarProcesoForm(request.POST)
        if form.is_valid():
            try:
                cedula = request.POST.get("cedula", '').strip()
                proceso = Proceso.objects.filter(cedula_contratista=cedula).first()
                estado = proceso.estado.__str__()
            except Exception as e:
                estado = "No encontrado"

            estado = estado.__str__()

    else:
        estado = ''
        form = RevisarProcesoForm()

    return render(request, 'formularioconsulta.html', {'form': form, 'estado': estado})
