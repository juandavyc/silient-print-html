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

        pdf = FPDF('P', 'mm', (75, 82))
        pdf.set_margins(top=2, left=2, right=5)
        pdf.set_auto_page_break(auto=False, margin=0)

        for i in range(0, 2):
            pdf.add_page()
            pdf.image('files/images/vigilado.jpg', x=1, y=2.6, w=30, h=10)
            pdf.set_font(family='helvetica', size=10)
            pdf.multi_cell(w=0, h=4, txt=self._configuracion['calidad'], align='R')
            pdf.ln(1)
            pdf.set_font(family='helvetica', size=15, style='B')
            pdf.multi_cell(w=0, h=4, txt='TICKET DE INGRESO', align='C')
            pdf.ln(1)
            pdf.set_font(family='helvetica', size=10)
            pdf.cell(w=0, h=4, txt=self._configuracion['cda'], align='C', ln=1)
            pdf.cell(w=0, h=4, txt=self._configuracion['nit'], align='C')
            pdf.ln()
            pdf.set_font(family='helvetica', size=20, style='B')
            pdf.cell(w=15, h=7, txt=' ', align='C')
            pdf.cell(w=45, h=7, txt=f"{rtm['placa'].upper()}", align='C')
            pdf.cell(w=7, h=7, txt=f"{rtm['vez']}", align='C', border=1)
            pdf.ln()
            pdf.set_font(family='helvetica', size=10)
            pdf.cell(w=0, h=5, txt=f"{rtm['fecha'].upper()}", align='C')
            pdf.ln()
            pdf.set_font(family='helvetica', size=12, style='B')
            pdf.cell(w=0, h=5, txt=f"{rtm['tipo']} {rtm['servicio']}", border='T', align='C')
            pdf.ln()
            pdf.set_font(family='helvetica', size=12, style='B')
            pdf.cell(w=0, h=5, txt=f"{rtm['kilometraje']} KM", border='B', align='C')
            pdf.ln(5)
            pdf.set_font(family='helvetica', size=12, style='B')
            pdf.image('files/images/side.jpg', x=1, y=50.5, w=6, h=14)
            pdf.cell(w=4, h=5, txt='')
            pdf.cell(w=73, h=5, txt=f"{rtm['telefono']}", ln=1)
            pdf.cell(w=4, h=5, txt='')
            pdf.cell(w=73, h=5, txt=f"{rtm['direccion']}", ln=1)
            pdf.cell(w=4, h=5, txt='')
            pdf.cell(w=73, h=5, txt=f"{rtm['correo']}")
            pdf.ln()
            pdf.set_font(family='helvetica', size=10, style='B')
            pdf.cell(w=0, h=5, txt=self._configuracion['anuncio']['uno'], align='C', border='T', ln=1)
            pdf.set_font(family='helvetica', size=10)
            pdf.cell(w=0, h=4, txt=self._configuracion['anuncio']['dos'], align='C', ln=1)
            pdf.set_font(family='helvetica', size=10, style='I')
            pdf.cell(w=0, h=4, txt=self._configuracion['footer'], align='C', ln=1)
        """
        pdf.add_page(format=(75, 25))
        pdf.set_font(family='helvetica', size=15, style='B')
        pdf.cell(w=0, h=7, txt=f"{rtm['placa'].upper()} - {rtm['kilometraje']} KM", align='C', border='B')
        pdf.ln()
        pdf.set_font(family='helvetica', size=10)
        pdf.cell(w=25, h=5, txt=f"Iz Delantera:")
        pdf.cell(w=12, h=5, txt=f"{rtm['psi'][0]}")
        pdf.cell(w=25, h=5, txt=f"De Delantera:")
        pdf.cell(w=12, h=5, txt=f"{rtm['psi'][1]}", ln=1)
        pdf.cell(w=25, h=5, txt=f"Iz Trasera:")
        pdf.cell(w=12, h=5, txt=f"{rtm['psi'][2]}")

        pdf.cell(w=25, h=5, txt=f"Iz Trasera:")
        pdf.cell(w=12, h=5, txt=f"{rtm['psi'][2]}")
        pdf.cell(w=25, h=5, txt=f"De Trasera:")
        pdf.cell(w=12, h=5, txt=f"{rtm['psi'][3]}", ln=1)
        pdf.cell(w=25, h=5, txt=f"Repuesto:")
        pdf.cell(w=12, h=5, txt=f"{rtm['psi'][4]}")
        """
        self.scroll_text('Plantilla PDF -> Terminada')
        pdf.output('files/temp/ticket_ingreso.pdf')
        self.pdf_printer(os.path.abspath(os.path.join("files", "temp", "ticket_ingreso.pdf")))
