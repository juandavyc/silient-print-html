import os

from fpdf import FPDF


class MakePDF(FPDF):

    def __init__(self, _configuracion, pdf_printer, scroll_text, ):
        self.pdf_printer = pdf_printer
        self.scroll_text = scroll_text
        # No modificar
        self._configuracion = _configuracion

    def crear_pdf(self, rtm):
        self.scroll_text('Plantilla PDF -> Iniciando')

        pdf = _PdfCustom('P', 'mm', (80, 180))
        pdf._custom_config(self._configuracion)

        pdf.alias_nb_pages()
        pdf.set_margins(top=5, left=2, right=5)
        pdf.set_auto_page_break(auto=False, margin=0)

        for i in range(0, 2):
            pdf.add_page()
            pdf.image('files/images/vigilado.jpg', x=3, y=5, w=30, h=11)
            pdf.set_font(family='Arial', size=10)
            pdf.multi_cell(w=0, h=4, txt=self._configuracion['calidad'], align='R')
            pdf.ln()
            pdf.set_font(family='Arial', size=17, style='B')
            pdf.multi_cell(w=0, h=9, txt='TICKET DE INGRESO', align='C')
            pdf.set_font(family='Arial', size=12)
            pdf.cell(w=0, h=5, txt=self._configuracion['cda'], align='C', ln=1)
            pdf.set_font(family='Arial', size=11)
            pdf.cell(w=0, h=5, txt=self._configuracion['nit'], align='C')
            pdf.ln(15)
            pdf.set_font(family='Arial', size=22, style='B')
            pdf.cell(w=15, h=7, txt=' ', align='C')
            pdf.cell(w=40, h=7, txt=f"{rtm['placa'].upper()}", align='C')
            pdf.cell(w=2, h=7, txt=' ')
            pdf.cell(w=10, h=11, txt=f"{rtm['vez']}", align='C', border=1)
            pdf.ln(6)
            pdf.set_font(family='Arial', size=11)
            pdf.cell(w=0, h=8, txt=f"{rtm['fecha'].upper()}", align='C')
            pdf.rect(x=10, y=63, w=60, h=0, style='DF')
            pdf.ln(11)
            pdf.image(f"files/images/{rtm['tipo'].lower()}.jpg", x=42, y=64)
            pdf.set_font(family='Arial', size=13, style='B')
            pdf.cell(w=5, h=5, txt=' ')
            pdf.multi_cell(w=0, h=5, txt=f"{rtm['tipo']}\n{rtm['servicio']}\n{rtm['kilometraje']} km", align='L')
            pdf.ln(7)
            pdf.rect(x=10, y=86, w=60, h=0, style='DF')

            pdf.set_font(family='Arial', size=11, style='I')
            pdf.cell(w=0, h=4, txt='Numero de celular WhatsApp', align='C', ln=1)
            pdf.set_font(family='Arial', size=14, style='B')
            pdf.cell(w=0, h=7, txt=f"{rtm['telefono']}", align='C', ln=1)

            pdf.set_font(family='Arial', size=11, style='I')
            pdf.cell(w=0, h=4, txt='Dirección', align='C', ln=1)
            pdf.set_font(family='Arial', size=14, style='B')
            pdf.multi_cell(w=0, h=7, txt=f"{rtm['direccion']}", align='C')

            pdf.set_font(family='Arial', size=11, style='I')
            pdf.cell(w=0, h=4, txt='Correo Electrónico', align='C', ln=1)
            pdf.set_font(family='Arial', size=14, style='B')
            pdf.multi_cell(w=0, h=7, txt=f"{rtm['correo'].upper()}", align='C')

        self.scroll_text('Plantilla PDF -> Terminada')
        pdf.output('files/temp/ticket_ingreso.pdf')
        self.pdf_printer(os.path.abspath(os.path.join("files","temp","ticket_ingreso.pdf")))



## Inner class
class _PdfCustom(FPDF):
    def _custom_config(self, config):
        self._configxd = config

    # Page footer
    def footer(self):
        self.set_y(-35)
        self.set_font(family='Arial', size=10, style='B')
        self.cell(w=0, h=7, txt=self._configxd['anuncio']['uno'], align='C')
        self.ln(5)
        self.set_font(family='Arial', size=10)
        self.cell(w=0, h=5, txt=self._configxd['anuncio']['dos'], align='C')
        self.ln(4)
        self.cell(w=0, h=5, txt=self._configxd['anuncio']['tres'], align='C')
        self.ln(4)
        self.set_font(family='Arial', size=10, style='B')
        self.cell(w=0, h=5, txt=self._configxd['anuncio']['cuatro'], align='C', ln=1)
        self.set_font(family='Arial', size=10, style='I')
        self.cell(w=75, h=7, txt=self._configxd['footer'], align='C')
        self.ln(4)
        self.set_font(family='Arial', size=8, style='B')
        self.cell(w=75, h=7, txt=self._configxd['proveedor'], align='C')
        self.ln(5)
        self.set_font(family='Arial', size=8, style='I')
        self.cell(0, 10, 'Page ' + str(self.page_no()) + ' / {nb}', 0, 0, 'C')
