from apps.contratacion.models import ProcesoEstados

variables_lista = {

    ProcesoEstados.REVISION: {
        "TITULO": "Listar Revision",
        "TITULO_HEADER": "Modulo de Radicacion",
        "RUTA": "Radicacion",
        "RUTA_DESC": "Listar procesos en revision",
        "URL": "radicacion/revision/",
    },
    ProcesoEstados.REVISIONMOD: {
        "TITULO": "Listar modificaciones en Revision",
        "TITULO_HEADER": "Modulo de Radicacion",
        "RUTA": "Radicacion",
        "RUTA_DESC": "Listar modificaciones en revision",
        "URL": "radicacion/editar_modificaciones/",
    },
    ProcesoEstados.REVISAR:{
        "TITULO": "Listar Revisar",
        "TITULO_HEADER": "Modulo de Alistamiento",
        "RUTA": "Alistamiento",
        "RUTA_DESC": "Listar procesos a revisar",
        "URL": "alistamiento/revisar/",
    },
    ProcesoEstados.REVISARMOD: {
        "TITULO": "Listar Revisar Modificaciones",
        "TITULO_HEADER": "Modulo de Alistamiento",
        "RUTA": "Alistamiento",
        "RUTA_DESC": "Listar modificaciones a revisar",
        "URL": "alistamiento/revisar_mod/",
    },
    ProcesoEstados.PRIMER_FLUJO: {
        "TITULO": "Listar Primer Flujo",
        "TITULO_HEADER": "Modulo de Alistamiento",
        "RUTA": "Alistamiento",
        "RUTA_DESC": "Listar procesos en Primer Flujo",
        "URL": "alistamiento/primer-flujo/",
    },
    ProcesoEstados.SUBSANACION: {
        "TITULO": "Listar Subsanacion",
        "TITULO_HEADER": "Modulo de Alistamiento",
        "RUTA": "Alistamiento",
        "RUTA_DESC": "Listar procesos en Subsanacion",
        "URL": "alistamiento/subsanacion/",
    },
    ProcesoEstados.NUMERACION_CONTRATO: {
        "TITULO": "Listar Numeracion",
        "TITULO_HEADER": "Modulo de Numeración de Procesos",
        "RUTA": "Estructuracion y Desarrollo",
        "RUTA_DESC": "Listar procesos para numerar",
        "URL": "numeracion/",
    },
    ProcesoEstados.SECOP_PUBLICACION: {
        "TITULO": "Listar Secop Publicacion",
        "TITULO_HEADER": "SECOP - PUBLICACIÓN",
        "RUTA": "Secop-publicacion",
        "RUTA_DESC": "Listar procesos en Secop Publicacion",
        "URL": "secop-publicacion/",
    },
    ProcesoEstados.SECOP_REVISAR: {
        "TITULO": "Listar Secop Revisar",
        "TITULO_HEADER": "SECOP - FLUJOS",
        "RUTA": "Secop-Flujos",
        "RUTA_DESC": "Listar procesos en estado Revisar",
        "URL": "secop-flujos/revisar/",
    },
    ProcesoEstados.SEGUNDO_FLUJO: {
        "TITULO": "Listar Segundo Flujo",
        "TITULO_HEADER": "SECOP - FLUJOS",
        "RUTA": "Secop-Flujos",
        "RUTA_DESC": "Listar procesos en Segundo Flujo",
        "URL": "secop-flujos/segundo-flujo/",
    },

    ProcesoEstados.SECOP_FIRMA: {
        "TITULO": "Listar Secop Firma",
        "TITULO_HEADER": "SECOP - FLUJOS",
        "RUTA": "Secop-Flujos",
        "RUTA_DESC": "Listar procesos en Secop Firma",
        "URL": "secop-flujos/secop-firma/",
    },

    ProcesoEstados.FIRMADO: {
        "TITULO": "Listar Firmados",
        "TITULO_HEADER": "Modulo de Tramites CRP",
        "RUTA": "Tramites CRP",
        "RUTA_DESC": "Listar procesos en Tramite",
        "URL": "tramite-crp/firmados/",
    },

    ProcesoEstados.SOLICITUD_CRP: {
        "TITULO": "Listar Solicitud CRP",
        "TITULO_HEADER": "Modulo de Tramites CRP",
        "RUTA": "Solicitud CRP",
        "RUTA_DESC": "Listar procesos  en Solicitud CRP",
        "URL": "tramite-crp/solicitud-crp/",
    },

    ProcesoEstados.TRAMITE_FINANCIERA: {
        "TITULO": "Listar Financiera",
        "TITULO_HEADER": "Modulo de Financiera",
        "RUTA": "Financiera",
        "RUTA_DESC": "Listar procesos en Financiera",
        "URL": "financiera/tramite/",
    },

    ProcesoEstados.PERFECCIONAMIENTO: {
        "TITULO": "Listar Perfeccionamiento",
        "TITULO_HEADER": "Modulo de Perfeccionamiento",
        "RUTA": "Perfeccionamiento",
        "RUTA_DESC": "Listar Procesos en Perfeccionamiento",
        "URL": "perfeccionamiento/",
    },
}


def getListFlow(modificacion):

    try:
        if variables_lista[modificacion]:
            return variables_lista[modificacion]
        
    except:
        return None