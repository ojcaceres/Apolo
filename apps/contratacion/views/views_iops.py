from django.http.response import HttpResponse
from django.utils import timezone
from apps.contratacion.models import Proceso
from django.shortcuts import render
from django.core import serializers

from django.views.decorators.csrf import csrf_exempt


# Create your views here.
# @api_view(['POST'])
@csrf_exempt
def iops_api(request):
    import traceback
    mensaje = 1  # "El usuario ha sido creado de manera correcta en Apolo HV"
    numero_contrato = request.GET['numero_contrato']
    vigencia = request.GET['vigencia']

    try:
        procesos = Proceso.objects.filter(numero_contrato=numero_contrato)
        proceso_inicial= procesos.get(modificacion="CONTRATO_INICIAL")
        mensaje = "Se encontraron " + str(procesos.count()) + " procesos de la vigencia " + vigencia
        for proceso in procesos:
            print(proceso.modificacion)
            print(proceso_inicial.id)
    except:
        mensaje = "No Se encontraron Procesos "
    return HttpResponse(mensaje)


"""
        IdContrato
        NumeroContrato
        Vigencia
        duración
        duracionInicial
        FechaContrato
        FechaInicio
        FechaFin
        IdDependencia
        Dependencia
        IdCentroCosto
        CodigoProyecto
        NombreProyecto
        TipoIdentificacion
        NumeroIdentificacion
        Nombre
        NombTipoContr
        ObjetoContrato
        codLocalidad
        nomLocalidad
        ValorContrato
        valorInicialContrato
        Obligaciones
        Presupuesto
        Modificaciones
"""


"""
Tipo complejo “Obligación”:
Nombre	Tipo	Descripción
Numero	Entero	Número secuencial de la obligación del contrato, comenzando en uno (1).
IdObligacion	Entero largo	Identificador interno de Apolo de la obligación
Contenido	Cadena de caracteres	Texto descriptivo de la obligación

Tipo complejo “Presupuesto”:
Nombre	Tipo	Descripción
NumCRP	Entero	Número del certificado de registro presupuestal
FecCRP	Fecha	Fecha de constitución del CRP
FechaInicio	Fecha	La fecha en la cual comienza la vigencia del CRP, la cual debe coincidir con:
•	Fecha de inicio del contrato, para CRPs que soportan el contrato inicial
•	Fecha de inicio de la adición, para CRPs que soportan las adiciones
IdContrato	Entero largo	El identificador interno de Apolo para el contrato (CRPs que soportan el contrato inicial) o la adición (CRPs que soportan las adiciones)
PresupuestoAdicion	Booleano	Determina si corresponde a un CRP de contrato inicial (false) o de adición (true)
CodProyecto	Entero	Código del proyecto asignado al CRP
NomProyecto	Cadena de caracteres	Nombre del proyecto asignado al CRP
CodConcepto	Entero largo	Código del concepto de gasto
NomConcepto	Cadena de caracteres	Nombre del concepto de gasto
CodFuente	Entero	Código de la fuente de financiación, de acuerdo con lo almacenado en Seven
NomFuente	Cadena de caracteres	Nombre de la fuente de financiación


Tipo complejo “Modificacion”:
Nombre	Tipo	Descripción
Adiciones	Arreglo de adición	Detalla las adiciones que han sido registradas para el contrato. Se entiende por adición la alteración del contrato para añadir plazo en días y valor monetario.
Cesiones	Arreglo de cesion	Detalla las cesiones que han sido registradas para el contrato. Se entiende por cesión la transferencia del contrato de una persona a otra.
Suspensiones	Arreglo de suspensión	Detalla las suspensiones que han sido registradas para el contrato. Se define como Suspensión temporal de las obligaciones contractuales, pactado de mutuo acuerdo entre las partes. La aplicación de una suspensión afecta la fecha de terminación del contrato
Terminaciones	Arreglo de terminación	Detalla las terminaciones anticipadas que han sido registradas para el contrato. Se define como Extinción de las obligaciones contractuales antes de la fecha final pactada inicialmente, llevada a cabo de manera unilateral o por mutuo acuerdo.
Prorrogas	Arreglo de prorroga	Detalla las prorrogas que han sido registradas para el contrato. Se entiende como prorroga la alteración del contrato para añadir plazo en días, pero sin añadir valor monetario.
Reducciones	Arreglo de reducción	Detalla las reducciones que han sido registradas para el contrato. Se entiende por reducción la alteración del contrato para disminuir el valor monetario del mismo.
Liberaciones	Arreglo de liberacion	Detalla los periodos en los cuales no se prestó servicio, pero no se constituyó una suspensión, por lo que de mutuo acuerdo entre las partes se indica el no pago de los días en el que el servicio no fue prestado, quedando un saldo a favor de la entidad.


Tipo complejo “Adicion”:
Nombre	Tipo	Descripción
Id	Entero largo	Identificador interno de Apolo
Fecha	Fecha y hora	Fecha en la que se registró la novedad en Apolo
Duración	Entero	Duración en días de la adición. El número de días corresponderá con el formato de año comercial de 360 días, donde cada mes corresponde a un total de 30 días.
FechaFirma	Fecha	La fecha en la que se firma la adición
FechaInicio	Fecha	La fecha de inicio de la adición
FechaFin	Fecha	La fecha de finalización de la adición
Valor	Decimal	El valor monetario de la adición.

Tipo complejo “Cesion”:
Nombre	Tipo	Descripción
Id	Entero largo	Identificador interno de Apolo
Fecha	Fecha y hora	Fecha en la que se registró la novedad en Apolo
DocumentoCedente	Entero largo	Número de documento de identificación del contratista que cede el contrato.
Cedente	Cadena de caracteres	Nombre del contratista que cede el contrato
DocumentoCesionario	Entero largo	Número de documento de identificación del contratista que toma el contrato.
Cesionario	Cadena de caracteres	Nombre del contratista que toma el contrato
FechaInicio	Fecha	Fecha a partir de la cual el cesionario toma el contrato

Tipo complejo “Suspension”:
Nombre	Tipo	Descripción
Id	Entero largo	Identificador interno de Apolo
Fecha	Fecha y hora	Fecha en la que se registró la novedad en Apolo
FechaInicio	Fecha	Fecha en la que inicia la suspensión, entendido como el primer día en el que se deja de prestar servicio.
FechaFin	Fecha	Fecha en la que se termina la suspensión, entendida como el último día en el cual no se prestará servicio.
FechaReinicio	Fecha	Fecha en la cual se procede a reiniciar la prestación del servicio y que corresponde al día posterior a la fecha de finalización de la suspensión.

Tipo complejo “Terminacion”:
Nombre	Tipo	Descripción
Id	Entero largo	Identificador interno de Apolo
Fecha	Fecha y hora	Fecha en la que se registró la novedad en Apolo
FechaInicio	Fecha	Fecha en la cual se termina el contrato, entendida como la última fecha en la cual se prestará el servicio.

Tipo complejo “Prorroga”:
Nombre	Tipo	Descripción
Id	Entero largo	Identificador interno de Apolo
Fecha	Fecha y hora	Fecha en la que se registró la novedad en Apolo
Duración	Entero	Duración en días de la prórroga. El número de días corresponderá con el formato de año comercial de 360 días, donde cada mes corresponde a un total de 30 días.
FechaFirma	Fecha	La fecha en la que se firma la prórroga
FechaInicio	Fecha	La fecha de inicio de la prórroga
FechaFin	Fecha	La fecha de finalización de la prórroga

Tipo complejo “Reduccion”:
Nombre	Tipo	Descripción
Id	Entero largo	Identificador interno de Apolo
Fecha	Fecha y hora	Fecha en la que se registró la novedad en Apolo
FechaFirma	Fecha	La fecha en la que se firma la reducción
FechaInicio	Fecha	La fecha de inicio de la reducción
Valor	Decimal	Valor a reducir el contrato

Tipo complejo “Liberacion”:
Nombre	Tipo	Descripción
Id	Entero largo	Identificador interno de Apolo
Fecha	Fecha y hora	Fecha en la que se registró la novedad en Apolo
FechaInicio	Fecha	Primer día en el que se deja de prestar servicio.
FechaFin	Fecha	Último día en el cual no se prestará servicio.
FechaReinicio	Fecha	Fecha en la cual se procede a reiniciar la prestación del servicio y que corresponde al día posterior a la fecha de finalización de la novedad.
Valor	Decimal	Valor para descontar y que quedará como saldo a liberar a favor de la entidad.
Duración	Entero	Duración en días del periodo de no prestación del servicio. El número de días corresponderá con el formato de año comercial de 360 días, donde cada mes corresponde a un total de 30 días.


Notas:
•	La especificación supone que Seven seguirá activo para el manejo presupuestal, razón por la cual no se solicitan valores como:
o	Saldo
o	Cuenta bancaria
o	Beneficiario asignado al CRP
o	Valor del CRP
o	Saldo actual del CRP
o	Código presupuestal del CRP
o	Nombre presupuestal del CRP


"""






