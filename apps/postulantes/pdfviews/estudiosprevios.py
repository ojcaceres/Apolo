from django.conf import settings
from io import BytesIO
from django.http import HttpResponse
from django.views.generic import View
from datetime import datetime

from reportlab.lib import colors, styles
from reportlab.platypus import SimpleDocTemplate, PageTemplate
from reportlab.platypus.frames import Frame
from functools import partial

from reportlab.platypus import Table, TableStyle, Frame
from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm, mm, inch

from apps.postulantes.pdfviews.textos import texto

class EstudiosPreviosPDF(View):

    def header(self, canvas, doc, content):
        canvas.saveState()
        w, h = content.wrap(doc.width, doc.topMargin)
        content.drawOn(canvas, doc.leftMargin + 3*mm, doc.height + doc.bottomMargin + doc.topMargin - h -10*mm)
        canvas.restoreState()

    def footer(self, canvas, doc, content):
        canvas.saveState()
        w, h = content.wrap(doc.width, doc.bottomMargin-150)
        content.drawOn(canvas, doc.leftMargin, 21)
        canvas.restoreState()

    def header_and_footer(self, canvas, doc, header_content, footer_content):
        self.header(canvas, doc, header_content)
        self.footer(canvas, doc, footer_content)

    def current_date_format(self, date):
        months = (
        "Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre",
        "Diciembre")
        day = date.day
        month = months[date.month - 1]
        year = date.year
        messsage = "{} de {} del {}".format(day, month, year)
        return messsage


    def separador(self, contenido, texto, centrado=None):
        contenido.append(Spacer(0, 4))
        estilogris = [
            ('GRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey)
        ]
        if centrado:
            estilogris = [
                ('GRID', (0, 0), (-1, -1), 0.25, colors.black),
                ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
                ('ALIGN', (0, 0), (-1, 0), "CENTER"),
            ]
        separador = Table([[texto]], colWidths=168 * mm, style=estilogris)
        contenido.append(separador)

    def encabezado(self, contenido):
        escudo_alcaldia = settings.MEDIA_ROOT + '/escudo.jpg'
        imagen_logo = Image(escudo_alcaldia, width=50, height=50)
        data = [
            [imagen_logo, 'SECRETARÍA DISTRITAL DE INTEGRACIÓN SOCIAL\nSUBDIRECCION DE CONTRATACION', '', '', '', '',
             ''],
            ['', '', '', '', '', '', '', ''],
            ['', 'PROCESO DE ADQUISICIONES PLANEAR LA ADQUISICION\nESTUDIOS PREVIOS', '', '', '', '', 'CÒDIGO', ''],
            ['', '', '', '', '', '', 'FECHA', ''],
            ['', '', '', '', '', '', 'VERSIÓN', ''],
            ['', '', '', '', '', '', 'PÀGINA', '1 de 1']]
        encabezado = Table(data, colWidths=21 * mm, rowHeights=5 * mm)
        encabezado.setStyle([('SPAN', (0, 0), (0, 5)),
                             ('SPAN', (1, 0), (7, 1)),
                             ('SPAN', (1, 2), (5, 5)),
                             ('ALIGN', (0, 0), (7, 5), 'CENTER'),
                             ('VALIGN', (0, 0), (7, 5), 'MIDDLE'),
                             ('FONTSIZE', (1, 0), (5, 5), 10),
                             ('FONTNAME', (1, 0), (5, 5), 'Helvetica-Bold'),
                             ('FONTSIZE', (6, 1), (7, 6), 7),
                             ('GRID', (0, 0), (-1, -1), 0.25, colors.black)
                             ])
        return encabezado

    def get(self, request, *args, **kwargs):

        #Temporalmente colocamos variables para entender que es lo que entra
        variable_nombre = "Alejandro Sastoque Sastoque Sastoque Sastoque Sastoque"
        variable_cargo = "Desarrollador"
        variable_objeto = "PRESTAR SERVICIOS PROFESIONALES COMO RESPONSABLE DEL SERVICIO PARA PROMOVER EL DESARROLLO INTEGRAL DE LA PRIMERA INFANCIA EN LOS SERVICIOS DE EDUCACIÃ“N INICIAL CON ENFOQUE DE ATENCIÃ“N INTEGRAL DE LA SDIS EN EL MARCO DEL SISTEMA DISTRITAL DE CUIDADO"
        variable_certificacion= "<para align=justify spaceb=3>Que el(la) suscrito(a) SUBDIRECTOR(A) DE GESTION Y DESARROLLO DEL TALENTO HUMANO DE LA SDIS, CONSIDERANDO que si bien la Secretaría Distrital de Integración Social cuenta con una Planta de Personal Global, el personal vinculado a la planta y los perfiles existentes no son suficientes para suplir las necesidades actuales de servicio de todos los Proyectos de la SDIS y sus coberturas, además el actual Manual Específico de Funciones y Competencias Laborales no contempla en todos los perfiles Asesores Profesionales Técnicos y Asistenciales el requisito de conocimientos especializados y específicos demandados en los diferentes Proyectos para el cumplimiento de los objetivos y ls Misión Institucional. En </para>"
        # Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        # La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        my_doc = SimpleDocTemplate(buffer, pagesize=letter,
                                   leftMargin=21*mm, rightMargin=21*mm,
                                   topMargin=38*mm, bottomMargin=30*mm)
        contenido = []
        self.separador(contenido, "1. DESCRIPCIÓN DE LA NECESIDAD QUE PRETENDE SATISFACER")
        contenido.append(Spacer(0, 10))
        data = [
            "var1 Robinson Moiscoso", 
            "var2 suba",  
            'var3 direccion de infancia', 
            'var 4AZ-vccfgf-0001',
        ]
        nombre = 'Robinson Moscoso'
        parra1=texto.parrafo1.format(*data)
        contenido.append(Paragraph("Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche "))
        contenido.append(Spacer(0, 10))

        contenido.append(Paragraph("Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche "))
        contenido.append(Spacer(0, 10))
        contenido.append(Paragraph("Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche "))
        contenido.append(Spacer(0, 10))
        contenido.append(Paragraph("Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche "))
        contenido.append(Spacer(0, 10))
        contenido.append(Paragraph("Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche "))
        contenido.append(Spacer(0, 10))
        contenido.append(Paragraph("Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche "))
        contenido.append(Spacer(0, 10))
        contenido.append(Paragraph("Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche "))
        contenido.append(Spacer(0, 10))
        contenido.append(Paragraph("Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche "))
        contenido.append(Spacer(0, 10))
        contenido.append(Paragraph("Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche "))
        contenido.append(Spacer(0, 10))
        contenido.append(Paragraph("Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche "))
        contenido.append(Spacer(0, 10))
        contenido.append(Paragraph("Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche "))
        contenido.append(Spacer(0, 10))
        contenido.append(Paragraph("Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche "))
        contenido.append(Spacer(0, 10))
        contenido.append(Paragraph("Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche Esta es una muestra para Cheche "))
        contenido.append(Spacer(0, 10))
        contenido.append(Paragraph(parra1))
        contenido.append(Spacer(0, 10))
        contenido.append(Paragraph(texto.parrafo2))
        contenido.append(Spacer(0, 10))
        contenido.append(Paragraph(texto.parrafo3))
        contenido.append(Spacer(0, 10))
        contenido.append(Paragraph(texto.parrafo4))
        contenido.append(Spacer(0, 10))
        contenido.append(Paragraph(texto.parrafo5))
        contenido.append(Spacer(0, 10))
        
        frame = Frame(my_doc.leftMargin, my_doc.bottomMargin, my_doc.width, my_doc.height, id='normal')
        header_content = self.encabezado(contenido)
        footer_img = settings.MEDIA_ROOT + '/footer.jpg'
        footer_content = Image(footer_img, width=168*mm, height=25*mm)
        template = PageTemplate(id='test', frames=frame,
                                onPage=partial(self.header_and_footer, header_content=header_content,
                                               footer_content=footer_content))
        my_doc.addPageTemplates([template])
        my_doc.build(contenido, onFirstPage=partial(self.header_and_footer, header_content=header_content,
                                                    footer_content=footer_content),
                     onLaterPages=partial(self.header_and_footer, header_content=header_content,
                                          footer_content=footer_content))
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)

        return response