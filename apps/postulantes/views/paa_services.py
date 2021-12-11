from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.files import File 

from Apolo.settings import APOLOHV_URL

import datetime

from xmltodict3 import XmlTextToDict

#import xmltodict

from requests import Session


import base64

def get_cdp_from_paa(vigencia_plan, numero_cdp, vigencia_cdp):
    import requests, json
    url_servicio = "http://pruebas.sdis.gov.co/reportes/WS/API/PAA/" + numero_cdp #"http://preproduccion.serviciocivil.gov.co:8585/sideapInteroperabilidad/webresourcesJSON/sdis/obtenerDatosBasicosSDIS"
    url_servicio = "http://pruebas.sdis.gov.co/reportes/WS/api/PAA/ByCDP/" + vigencia_plan + "/" + numero_cdp + "-" + vigencia_cdp #"http://pruebas.sdis.gov.co/reportes/WS/API/PAA/" + numero_cdp #"http://preproduccion.serviciocivil.gov.co:8585/sideapInteroperabilidad/webresourcesJSON/sdis/obtenerDatosBasicosSDIS"
    respueasta = requests.get(url_servicio, data = {})
    if respueasta.text:
        data = respueasta.text
        data = json.loads(respueasta.text)
        return data
        # print(data)
        # result = XmlTextToDict(data, ignore_namespace=True).get_dict()
    else:
        return []

    # #http://pruebas.sdis.gov.co/reportes/WS/API/PAA/
    # text = '''
    # <RegistroPAA xmlns:i="http://www.w3.org/2001/XMLSchema-instance"
    # xmlns="http://schemas.datacontract.org/2004/07/SDIS.SII.Reportes.CapaNegocio.Entidades">
    # <CodActividad>037744020206</CodActividad>
    # <CodComponenteGasto>Servicios para la comunidad, sociales y personales</CodComponenteGasto>
    # <CodFuenteFinanciacion>02168</CodFuenteFinanciacion>
    # <CodMeta>179</CodMeta>
    # <CodPMR>13</CodPMR>
    # <CodProyecto>7744</CodProyecto>
    # <CodRubroPresupuestal>33116067744130206203</CodRubroPresupuestal>
    # <CodServicio>203</CodServicio>
    # <ComponenteGasto>10820105</ComponenteGasto>
    # <CompromisosConAutorizacionDeGiros>0</CompromisosConAutorizacionDeGiros>
    # <CompromisosSinAutorizacionDeGiro>18024000,00</CompromisosSinAutorizacionDeGiro>
    # <CupoConVigenciaFutura>No</CupoConVigenciaFutura>
    # <Dependencia>124</Dependencia>
    # <DescripcionCentroDeCosto>LOCALIDAD DE PUENTE ARANDA</DescripcionCentroDeCosto>
    # <DescripcionCupo>7744-RRHH-CI-0312</DescripcionCupo>
    # <DescripcionObjeto>PRESTAR SERVICIOS DE APOYO A LA GESTIÓN PARA PROMOVER EL DESARROLLO INTEGRAL DE LA PRIMERA
    #     INFANCIA EN LOS SERVICIOS DE EDUCACIÓN INICIAL CON ENFOQUE DE ATENCIÓN INTEGRAL DE LA SDIS EN EL MARCO DEL
    #     SISTEMA DISTRITAL DE CUIDADO</DescripcionObjeto>
    # <Ejecucion>0,00</Ejecucion>
    # <EstadoCupo>Activo</EstadoCupo>
    # <FechaDeCdp>26/02/2021; 02/03/2021; 04/03/2021; 04/03/2021; 05/03/2021; 05/03/2021</FechaDeCdp>
    # <FechaDeGiros></FechaDeGiros>
    # <FechaDeSolicitudDeCdp>23/02/2021; 23/02/2021; 23/02/2021; 23/02/2021; 23/02/2021; 23/02/2021
    # </FechaDeSolicitudDeCdp>
    # <FechaEstimadaCompra></FechaEstimadaCompra>
    # <FechaEstimadaPago></FechaEstimadaPago>
    # <FechaEstimadaProceso></FechaEstimadaProceso>
    # <FechaRadicacion></FechaRadicacion>
    # <FuenteFinanciacion>2-100-I009 - VA-SGP PROPÓSITO GENERAL</FuenteFinanciacion>
    # <HistoricoCaso>No incluido</HistoricoCaso>
    # <IdCupo>89698</IdCupo>
    # <Localidad>16</Localidad>
    # <ModalidadDeAdquisicion>1</ModalidadDeAdquisicion>
    # <ModalidadDeSeleccion>022</ModalidadDeSeleccion>
    # <Modificaciones>27036000,00</Modificaciones>
    # <NombreActividad>Atender con enfoque diferencial y con proyectos pedagógicos actualizados a las niñas y niños a
    #     través del servicio social en Jar</NombreActividad>
    # <NombreDependencia>SUBDIRECCION PARA LA INFANCIA</NombreDependencia>
    # <NombreMeta>0377440202-Atender a 71.000 niñas y niños con enfoque diferencial y de género, en servicios dirigidos a
    #     la primera infancia pertinentes y de calidad en el marco de la atención integral, a través de una oferta
    #     flexible que tenga en cuenta las dinámicas socioeconómicas de las familias y cuidadores/as, que permita
    #     potenciar su desarrollo, así como prevenir situaciones de riesgo para la garantía de derechos.</NombreMeta>
    # <NombreModalidadAdquisicion>RECURSO HUMABNO RH SDIS</NombreModalidadAdquisicion>
    # <NombreModalidadSeleccion>PRESTACIÓN DE SERVICIOS DE APOYO A LA GESTIÓN</NombreModalidadSeleccion>
    # <NombrePMR>ATENCIÓN INTEGRAL A NIÑOS, NIÑAS, ADOLESCENTES Y MUJERES GESTANTES EN LOS SERVICIOS DIRIGIDOSA LA
    #     POBLACIÓN DESDE LA GESTACIÓN HASTA LOS 17 AÑOS</NombrePMR>
    # <NombrePlan>Un Nuevo Contrato Social y Ambiental para la Bogotá del Siglo XXI</NombrePlan>
    # <NombreRubroPrespupuestal>Atender con enfoque diferencial y con proyectos pedagogicos actualizados a las ninas y
    #     ninos a traves del servicio social en Jardines Infantiles Diurnos, Nocturnos y Casas de Pensamiento
    #     Intercultural -SDIS, generando un acceso sin barreras</NombreRubroPrespupuestal>
    # <NombreServicio>Atención integral de niños y niñas en Jardines SDIS</NombreServicio>
    # <NombreTipoDeContratacion>CONTRATACION DIRECTA - MINUTA PERSONA NATURAL</NombreTipoDeContratacion>
    # <NompreProyecto>Generación de Oportunidades para el Desarrollo Integral de la Niñez y la Adolescencia de Bogotá
    # </NompreProyecto>
    # <NumeroCDP>6.845; 7.409; 8.058; 8.060; 8.138; 8.159</NumeroCDP>
    # <NumeroDeCaso>95.764; 97.046; 97.049; 97.203; 97.513; 98.033</NumeroDeCaso>
    # <NumeroDeContrato>4330; 3533; 4553; 4359</NumeroDeContrato>
    # <NumeroDelCrp>4.754; 5.859; 6.198; 5.858</NumeroDelCrp>
    # <ObjetoDelContrato>PRESTAR SERVICIOS DE APOYO A LA GESTIÓN PARA PROMOVER EL DESARROLLO INTEGRAL DE LA PRIMERA
    #     INFANCIA EN LOS SERVICIOS DE EDUCACIÓN INICIAL CON ENFOQUE DE ATENCIÓN INTEGRAL DE LA SDIS EN EL MARCO DEL
    #     SISTEMA DISTRITAL DE CUIDADO
    # ; PRESTAR SERVICIOS DE APOYO A LA GESTIÓN  PARA PROMOVER EL DESARROLLO INTEGRAL DE LA PRIMERA INFANCIA EN LOS SERVICIOS DE EDUCACIÓN INICIAL CON ENFOQUE DE ATENCIÓN INTEGRAL DE LA SDIS EN EL MARCO DEL SISTEMA DISTRITAL DE CUIDADO
    # ; PRESTAR SERVICIOS DE APOYO A LA GESTIÓN  PARA PROMOVER EL DESARROLLO INTEGRAL DE LA PRIMERA INFANCIA EN LOS SERVICIOS DE EDUCACIÓN INICIAL CON ENFOQUE DE ATENCIÓN INTEGRAL DE LA SDIS EN EL MARCO DEL SISTEMA DISTRITAL DE CUIDADO
    # ; PRESTAR SERVICIOS DE APOYO A LA GESTIÓN  PARA PROMOVER EL DESARROLLO INTEGRAL DE LA PRIMERA INFANCIA EN LOS SERVICIOS DE EDUCACIÓN INICIAL CON ENFOQUE DE ATENCIÓN INTEGRAL DE LA SDIS EN EL MARCO DEL SISTEMA DISTRITAL DE CUIDADO
    # </ObjetoDelContrato>
    # <Plazo></Plazo>
    # <PresupuestoProgramado>0,00</PresupuestoProgramado>
    # <PresupuestoVigente>27036000,00</PresupuestoVigente>
    # <SaldoDeCupoDespuesDeCdp>0,00</SaldoDeCupoDespuesDeCdp>
    # <SaldoDeDisponibilidadesPorComprometer>9012000,00</SaldoDeDisponibilidadesPorComprometer>
    # <Tipo>Individual</Tipo>
    # <TipoDeContratacion>25</TipoDeContratacion>
    # <UNSPSC>80111500</UNSPSC>
    # <UnidadOperativa>13333316</UnidadOperativa>
    # <ValorCDP>27036000,00</ValorCDP>
    # <ValorDelCrp>18024000,00</ValorDelCrp>
    # <Vigencia>2021</Vigencia>
    # </RegistroPAA>
    # '''

    # result = XmlTextToDict(text, ignore_namespace=True).get_dict()

    # return result
