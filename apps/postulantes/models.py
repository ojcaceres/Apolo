from django.db import models
from apps.autenticacion.models import USUARIO
from apps.estructura.models import Estado
from apps.contratacion.models import ProcesoEstados, Proceso


# Create your models here.
class radicacion_postulante(models.Model):
    usuario = models.ForeignKey(USUARIO, on_delete= models.CASCADE, null=True, default=None, related_name="usuario_postulante")
    estado = models.ForeignKey(Estado, on_delete= models.CASCADE, to_field='nombre', default=ProcesoEstados.CREACION_RH)
    proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE, null=True, default=None)
    idpersonasideap = models.IntegerField()
    param_tipo_documento = models.IntegerField()
    param_tipo_documento_text = models.CharField(max_length=100)
    numero_documento = models.CharField(max_length=100)
    primer_nombre = models.CharField(max_length=100)
    segundo_nombre = models.CharField(max_length=100)
    primer_apellido = models.CharField(max_length=100)
    segundo_apellido = models.CharField(max_length=100)
    correoelectronicopersonal = models.CharField(max_length=100)
    param_codsexopersona = models.IntegerField()
    param_codsexopersona_text = models.CharField(max_length=100)
    id_pais_nacimiento = models.CharField(max_length=100)
    id_municipio_nacimiento = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    tiene_libreta_militar = models.BooleanField()
    direccion_residencia = models.CharField(max_length=250)
    num_telefono_domicilio = models.CharField(max_length=100)
    id_estado = models.IntegerField(default=1)
    id_directorio_azdigital = models.IntegerField(default=0)

    def __str__(self):
        return  "{0}:{1} - {2} {3} {4} {5}".format(self.param_tipo_documento_text, 
        self.numero_documento, self.primer_nombre, self.segundo_nombre, self.primer_apellido, self.segundo_apellido)

    def display_estado(self):
        estado = "Documentos Solicitados"
        if (self.id_estado == 1):
            estado = "Documentos Solicitados"
        elif (self.id_estado == 2):
            estado = "Documentos cargados"
        elif (self.id_estado == 3):
            estado = "En subsanacion"
        elif (self.id_estado == 4):
            estado = "Subsanacion a revisar"
        elif (self.id_estado == 5):
            estado = "Aprobados"
        elif (self.id_estado == 6):
            estado = "Desistido"
        return estado

    class Meta:
        db_table = 'radicacion_postulante'

class radicacion_cdp(models.Model):
    usuario = models.ForeignKey(USUARIO, on_delete= models.CASCADE, null=True, default=None,
                                related_name="usuario_cdp")
    estado = models.ForeignKey(Estado, on_delete= models.CASCADE, to_field='nombre', default=ProcesoEstados.CREACION_RH)
    proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE, null=True, default=None,)
    numero_cdp = models.IntegerField()
    vigencia_cdp = models.IntegerField()
    vigencia_plan_cdp = models.IntegerField()
    valor_cdp = models.DecimalField(max_digits=24, decimal_places=2)
    valor_afectacion = models.DecimalField(max_digits=24, decimal_places=2, default=0)
    honorarios = models.DecimalField(max_digits=24, decimal_places=2)
    valor_contrato = models.DecimalField(max_digits=24, decimal_places=2)
    codigo_proyecto  = models.CharField(max_length=100)
    id_cupo_paa = models.CharField(max_length=100)
    descripcion_cupo = models.CharField(max_length=500)
    descripcion_objeto = models.TextField()
    nombre_proyecto= models.CharField(max_length=500)
    nuemero_caso = models.CharField(max_length=100)
    id_radicacion_postulante = models.IntegerField()
    idpersonasideap = models.IntegerField()
    id_estado = models.IntegerField(default=1)

    def display_postulante(self):
        p = radicacion_postulante.objects.get(id = self.id_radicacion_postulante)
        nombre =   "{0}:{1} - {2} {3} {4} {5}".format(p.param_tipo_documento_text, 
        p.numero_documento, p.primer_nombre, p.segundo_nombre, p.primer_apellido, p.segundo_apellido)        
        return  nombre

    class Meta:
        db_table = 'radicacion_cdp'


# Create your models here.
class parametricas(models.Model):
    categoria = models.CharField(max_length=100) 
    valor = models.CharField(max_length=100)
    texto = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    cateogoria_padre = models.CharField(max_length=100)
    valor_padre = models.CharField(max_length=100)
    orden = models.IntegerField()
    deleted_at= models.DateField()
    created_at = models.DateField()
    updated_at = models.DateField()
    deleted_by = models.IntegerField()
    created_by = models.IntegerField()
    updated_by = models.IntegerField()

    def __str__(self):
        return "{0} [{1}] [{2}]".format(self.categoria, self.texto, self.valor)

    class Meta:
        db_table = 'estructura_parametricas'


class cargos_dependencias(models.Model):
    cargo = models.CharField(max_length=500)
    dependencia = models.CharField(max_length=500)
    nombre_completo = models.CharField(max_length=500)
    correo_institucional = models.CharField(max_length=500)
    activo = models.IntegerField( default=1)
    fecha_inicio = models.DateField()
    fecha_terminacion = models.DateField()
    observaciones = models.TextField()
    id_az_digital = models.CharField(max_length=100)
    deleted_at= models.DateField()
    created_at = models.DateField()
    updated_at = models.DateField()
    deleted_by = models.IntegerField()
    created_by = models.IntegerField()
    updated_by = models.IntegerField()

    def __str__(self):
        return "{0} - {1} ".format(self.dependencia, self.cargo)

    class Meta:
        db_table = 'estructura_cargos_dependencias'
        ordering = ['dependencia']


class radicacion_cdp_documentos(models.Model):
    id_radicacion_cdp = models.IntegerField()
    id_estructura_cargos_dependencias_remitente = models.IntegerField()
    nombre_remitente = models.CharField(max_length=500, default="")
    cargo_remitente = models.CharField(max_length=500, default="")
    dependencia_remitente = models.CharField(max_length=500, default="")
    id_estructura_cargos_destinatario = models.IntegerField()
    unidad_operativa = models.CharField(max_length=500, default="")
    nombre_destinatario = models.CharField(max_length=500, default="")
    cargo_destinatario = models.CharField(max_length=500, default="")
    dependencia_destinatario = models.CharField(max_length=500, default="")
    objeto = models.TextField(default="")
    experiencia_relacionada = models.TextField(default="")
    formacion_academica = models.TextField(default="")
    equipo_elabora = models.TextField(default="")
    reviso = models.CharField(max_length=500, default="")
    aprobo = models.CharField(max_length=500, default="")
    descripcion_necesidad = models.TextField(default="")
    objetivo = models.TextField(default="")
    meta = models.TextField(default="")
    alcance_objeto = models.TextField(default="")
    descripcion_rubro = models.TextField(default="")
    obligaciones_especificas = models.TextField(default="")
    numero_cdp = models.CharField(max_length=500, default="")
    numero_proyecto = models.CharField(max_length=500, default="")
    valor_cdp = models.DecimalField(max_digits=24, decimal_places=2 )
    valor_afectado = models.DecimalField(max_digits=24, decimal_places=2 )
    es_regimen_comun = models.IntegerField()
    plazo_ejecucion_meses = models.IntegerField()
    plazo_ejecucion_meses_letras = models.CharField(max_length=250, default="")
    plazo_ejecucion_dias = models.IntegerField()
    plazo_ejecucion_dias_letras = models.CharField(max_length=250, default="")
    valor_total_contrato_letras = models.CharField(max_length=250, default="")
    valor_mensual_contrato_letras = models.CharField(max_length=250, default="")
    aplican_garantias = models.IntegerField()
    aplica_paragrafo_suspension = models.IntegerField(default=0)
    cargo_supervisor = models.CharField(max_length=500, default="")
    dependencia_supervisor = models.CharField(max_length=500, default="")

    fecha_expedicion = models.DateField(auto_now_add=True, blank=True)

    class Meta:
        db_table = 'radicacion_cdp_documentos'