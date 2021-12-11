from apps.contratacion.models import ProcesoEstados

_flujos = {

    "OTROSI":{
        "CREACION_DE_LA_PRORROGA": {"next": ProcesoEstados.REVISION, "back": None},
        "REVISIONMOD": {"next": ProcesoEstados.REVISAR, "back": None, "action": "Save"},
        "REVISAR": {"next": ProcesoEstados.SECOP_PUBLICACION, "back": ProcesoEstados.SUBSANACION},
        "SUBSANACION": {"next": ProcesoEstados.REVISAR, "back": None},
        "SECOP_PUBLICACION": {"next": ProcesoEstados.SECOP_FIRMA, "back": ProcesoEstados.REVISAR, "action": ProcesoEstados.RECHAZADO},
        "SECOP_FIRMA": {"next": ProcesoEstados.PERFECCIONAMIENTO, "back": None, "action": ProcesoEstados.RECHAZADO},
        "PERFECCIONAMIENTO": {"next": None, "back": None},
    },

    "ADICION":{
        "CREACION_DE_LA_PRORROGA": {"next": ProcesoEstados.REVISION, "back": None},
        "REVISIONMOD": {"next": ProcesoEstados.REVISAR, "back": None, "action": "Save"},
        "REVISAR": {"next": ProcesoEstados.SECOP_PUBLICACION, "back": ProcesoEstados.SUBSANACION},
        "SUBSANACION": {"next": ProcesoEstados.REVISAR, "back": None},
        "SECOP_PUBLICACION": {"next": ProcesoEstados.SECOP_FIRMA, "back": ProcesoEstados.REVISAR, "action": ProcesoEstados.RECHAZADO},
        "SECOP_FIRMA": {"next": ProcesoEstados.SOLICITUD_CRP, "back": None, "action": ProcesoEstados.RECHAZADO},
        "SOLICITUD_CRP": {"next": ProcesoEstados.TRAMITE_FINANCIERA, "back": ProcesoEstados.REVISAR, "action": ProcesoEstados.RECHAZADO},
        "TRAMITE_FINANCIERA": {"next": ProcesoEstados.PERFECCIONAMIENTO, "back": None},
        "PERFECCIONAMIENTO": {"next": None, "back": None},
    },

        "CESION":{
        "CREACION_DE_LA_PRORROGA": {"next": ProcesoEstados.REVISION, "back": None},
        "REVISIONMOD": {"next": ProcesoEstados.REVISAR, "back": None, "action": "Save"},
        "REVISAR": {"next": ProcesoEstados.SECOP_PUBLICACION, "back": ProcesoEstados.SUBSANACION},
        "SUBSANACION": {"next": ProcesoEstados.REVISAR, "back": None},
        "SECOP_PUBLICACION": {"next": ProcesoEstados.SECOP_FIRMA, "back": ProcesoEstados.REVISAR, "action": ProcesoEstados.RECHAZADO},
        "SECOP_FIRMA": {"next": ProcesoEstados.PERFECCIONAMIENTO, "back": None, "action": ProcesoEstados.RECHAZADO},
        "PERFECCIONAMIENTO": {"next": None, "back": None},
    },

    "PRORROGA":{
        "CREACION_DE_LA_PRORROGA": {"next": ProcesoEstados.REVISION, "back": None},
        "REVISIONMOD": {"next": ProcesoEstados.REVISAR, "back": None, "action": "Save"},
        "REVISAR": {"next": ProcesoEstados.SECOP_PUBLICACION, "back": ProcesoEstados.SUBSANACION},
        "SUBSANACION": {"next": ProcesoEstados.REVISAR, "back": None},
        "SECOP_PUBLICACION": {"next": ProcesoEstados.SECOP_FIRMA, "back": ProcesoEstados.REVISAR, "action": ProcesoEstados.RECHAZADO},
        "SECOP_FIRMA": {"next": ProcesoEstados.PERFECCIONAMIENTO, "back": None, "action": ProcesoEstados.RECHAZADO},
        "PERFECCIONAMIENTO": {"next": None, "back": None},
    },

    "SUSPENSION":{
        "CREACION_DE_LA_PRORROGA": {"next": ProcesoEstados.REVISION, "back": None},
        "REVISIONMOD": {"next": ProcesoEstados.REVISAR, "back": None, "action": "Save"},
        "REVISAR": {"next": ProcesoEstados.SECOP_PUBLICACION, "back": ProcesoEstados.SUBSANACION},
        "SUBSANACION": {"next": ProcesoEstados.REVISAR, "back": None},
        "SECOP_PUBLICACION": {"next": ProcesoEstados.SECOP_FIRMA, "back": ProcesoEstados.REVISAR, "action": ProcesoEstados.RECHAZADO},
        "SECOP_FIRMA": {"next": ProcesoEstados.PERFECCIONAMIENTO, "back": None, "action": ProcesoEstados.RECHAZADO},
        "PERFECCIONAMIENTO": {"next": None, "back": None},
    },

    "REINICIO":{
        "CREACION_DE_LA_PRORROGA": {"next": ProcesoEstados.REVISION, "back": None},
        "REVISIONMOD": {"next": ProcesoEstados.REVISAR, "back": None, "action": "Save"},
        "REVISAR": {"next": ProcesoEstados.SECOP_PUBLICACION, "back": ProcesoEstados.SUBSANACION},
        "SUBSANACION": {"next": ProcesoEstados.REVISAR, "back": None},
        "SECOP_PUBLICACION": {"next": ProcesoEstados.SECOP_FIRMA, "back": ProcesoEstados.REVISAR, "action": ProcesoEstados.RECHAZADO},
        "SECOP_FIRMA": {"next": ProcesoEstados.PERFECCIONAMIENTO, "back": None, "action": ProcesoEstados.RECHAZADO},
        "PERFECCIONAMIENTO": {"next": None, "back": None},
    },

    "ADICION_PRORROGA":{
        "CREACION_DE_LA_PRORROGA": {"next": ProcesoEstados.REVISION, "back": None},
        "REVISIONMOD": {"next": ProcesoEstados.REVISAR, "back": None, "action": "Save"},
        "REVISAR": {"next": ProcesoEstados.SECOP_PUBLICACION, "back": ProcesoEstados.SUBSANACION},
        "SUBSANACION": {"next": ProcesoEstados.REVISAR, "back": None},
        "SECOP_PUBLICACION": {"next": ProcesoEstados.SECOP_FIRMA, "back": ProcesoEstados.REVISAR, "action": ProcesoEstados.RECHAZADO},
        "SECOP_FIRMA": {"next": ProcesoEstados.SOLICITUD_CRP, "back": None, "action": ProcesoEstados.RECHAZADO},
        "SOLICITUD_CRP": {"next": ProcesoEstados.TRAMITE_FINANCIERA, "back": ProcesoEstados.REVISAR, "action": ProcesoEstados.RECHAZADO},
        "TRAMITE_FINANCIERA": {"next": ProcesoEstados.PERFECCIONAMIENTO, "back": None},
        "PERFECCIONAMIENTO": {"next": None, "back": None},
    },

    "ADICION_PRORROGA_OTROSI":{
        "CREACION_DE_LA_PRORROGA": {"next": ProcesoEstados.REVISION, "back": None},
        "REVISIONMOD": {"next": ProcesoEstados.REVISAR, "back": None, "action": "Save"},
        "REVISAR": {"next": ProcesoEstados.SECOP_PUBLICACION, "back": ProcesoEstados.SUBSANACION},
        "SUBSANACION": {"next": ProcesoEstados.REVISAR, "back": None},
        "SECOP_PUBLICACION": {"next": ProcesoEstados.SECOP_FIRMA, "back": ProcesoEstados.REVISAR,
                             "action": ProcesoEstados.RECHAZADO},
        "SECOP_FIRMA": {"next": ProcesoEstados.SOLICITUD_CRP, "back": None, "action": ProcesoEstados.RECHAZADO},
        "SOLICITUD_CRP": {"next": ProcesoEstados.TRAMITE_FINANCIERA, "back": ProcesoEstados.REVISAR, "action": ProcesoEstados.RECHAZADO},
        "TRAMITE_FINANCIERA": {"next": ProcesoEstados.PERFECCIONAMIENTO, "back": None},
        "PERFECCIONAMIENTO": {"next": None, "back": None},
    },

    "ADICION_PRORROGA_SUSPENSION":{
        "CREACION_DE_LA_PRORROGA": {"next": ProcesoEstados.REVISION, "back": None},
        "REVISIONMOD": {"next": ProcesoEstados.REVISAR, "back": None, "action": "Save"},
        "REVISAR": {"next": ProcesoEstados.SECOP_PUBLICACION, "back": ProcesoEstados.SUBSANACION},
        "SUBSANACION": {"next": ProcesoEstados.REVISAR, "back": None},
        "SECOP_PUBLICACION": {"next": ProcesoEstados.SECOP_FIRMA, "back": ProcesoEstados.REVISAR,
                             "action": ProcesoEstados.RECHAZADO},
        "SECOP_FIRMA": {"next": ProcesoEstados.SOLICITUD_CRP, "back": None, "action": ProcesoEstados.RECHAZADO},
        "SOLICITUD_CRP": {"next": ProcesoEstados.TRAMITE_FINANCIERA, "back": ProcesoEstados.REVISAR, "action": ProcesoEstados.RECHAZADO},
        "TRAMITE_FINANCIERA": {"next": ProcesoEstados.PERFECCIONAMIENTO, "back": None},
        "PERFECCIONAMIENTO": {"next": None, "back": None},
    },

    "TERMINACION_ANTICIPADA":{
        "CREACION_DE_LA_PRORROGA": {"next": ProcesoEstados.REVISION, "back": None},
        "REVISIONMOD": {"next": ProcesoEstados.REVISAR, "back": None, "action": "Save"},
        "REVISAR": {"next": ProcesoEstados.SECOP_PUBLICACION, "back": ProcesoEstados.SUBSANACION},
        "SUBSANACION": {"next": ProcesoEstados.REVISAR, "back": None},
        "SECOP_PUBLICACION": {"next": ProcesoEstados.SECOP_FIRMA, "back": ProcesoEstados.REVISAR,
                             "action": ProcesoEstados.RECHAZADO},
        "SECOP_FIRMA": {"next": ProcesoEstados.PERFECCIONAMIENTO, "back": None, "action": ProcesoEstados.RECHAZADO},
        "PERFECCIONAMIENTO": {"next": None, "back": None},
    },

    "CONTRATO_INICIAL":{
        "CREACION_DEL_PROCESO": {"next": ProcesoEstados.REVISION, "back": None},
        "REVISION": {"next": ProcesoEstados.REVISAR, "back": None},
        "REVISAR": {"next": ProcesoEstados.PRIMER_FLUJO, "back": ProcesoEstados.SUBSANACION},
        "PRIMER_FLUJO": {"next": ProcesoEstados.NUMERACION_CONTRATO, "back": ProcesoEstados.SUBSANACION},
        "DEVUELTO_ALISTAMIENTO": {"next": ProcesoEstados.REVISAR, "back": None},
        "SUBSANACION": {"next": ProcesoEstados.REVISAR, "back": None},
        "NUMERACION_CONTRATO": {"next": ProcesoEstados.SECOP_PUBLICACION, "back": ProcesoEstados.REVISAR},
        "SECOP_PUBLICACION": {"next": ProcesoEstados.SECOP_REVISAR, "back": ProcesoEstados.REVISAR, "action": "Save"},
        "SECOP_REVISAR": {"next": ProcesoEstados.SEGUNDO_FLUJO, "back": None, "action": ProcesoEstados.RECHAZADO},
        "SEGUNDO_FLUJO": {"next": ProcesoEstados.SOLICITUD_CRP, "back": None, "action": ProcesoEstados.RECHAZADO},
        "SOLICITUD_CRP": {"next": ProcesoEstados.TRAMITE_FINANCIERA, "back": ProcesoEstados.REVISAR, "action": ProcesoEstados.RECHAZADO},
        "TRAMITE_FINANCIERA": {"next": ProcesoEstados.PERFECCIONAMIENTO, "back": ProcesoEstados.SOLICITUD_CRP},
        "PERFECCIONAMIENTO": {"next": None, "back": None},
    }
}


def getNext(modificacion, estado):
     return _getState('next', modificacion, estado)


def getBack(modificacion, estado):
    return _getState('back', modificacion, estado)


def _getState(process, modificacion, estado ):
    return getFlow(modificacion, estado)[process]


def getFlow(modificacion, estado):
    
    try: 
        if _flujos[modificacion]:
            
            if _flujos[modificacion][estado]:
                return _flujos[modificacion][estado];
        
    except: return {"next": None, "back": None}