import datetime
import json

from pdf.SocketThread import SocketThread
from pdf.MakePDF import MakePDF
from pdf.PrintService import PrintService


class Model:

    def __init__(self):
        self.scroll_text = None
        self.socket_estado = None

        self.pdf_ingreso = None
        self.pdf_socket = None
        self.pdf_printer = None

        self._archivo_configuracion = 'files/config.json'
        self._contador_scroll = 0
        self._data_configuracion = None
        self._leer_configuracion(self._archivo_configuracion)

    def main(self):

        self.pdf_printer = PrintService(
            {
                'impresora': self._data_configuracion['impresora'],
            },
            self.scroll_text
        )

        self.pdf_ingreso = MakePDF(
            {
                'calidad': self._data_configuracion['calidad'],
                'cda': self._data_configuracion['cda'],
                'nit': self._data_configuracion['nit'],
                'anuncio': self._data_configuracion['anuncio'],
                'footer': self._data_configuracion['footer'],
                'proveedor': self._data_configuracion['proveedor'],
            },
            self.pdf_printer.imprimir,
            self.scroll_text
        )
        self.pdf_socket = SocketThread(
            {
                'ip': self._data_configuracion['ip'],
                'puerto': self._data_configuracion['puerto'],
            },
            self.pdf_ingreso.crear_pdf,
            self.socket_estado,
            self.scroll_text
        )

        self.pdf_socket.start()

    def scroll_insert(self, scroll_text):
        self.scroll_text = scroll_text

    def socket_insert(self, socket_estado):
        self.socket_estado = socket_estado

    def get_date_time(self):
        now = datetime.datetime.now()
        return now.strftime("%H:%M:%S")

    def _leer_configuracion(self, src):
        with open(src, 'r', encoding='utf8') as archivo:
            self._data_configuracion = json.load(archivo)

    def guardar_configuracion(self):
        try:
            with open(self._archivo_configuracion, 'w', encoding='utf8') as archivo:
                archivo.write(json.dumps(self._data_configuracion, indent=4))
                return True
        except EnvironmentError:
                return False

    def limpiar_scroll_text(self):
        self._contador_scroll += 1
        if self._contador_scroll == 100:
            self._contador_scroll = 0
            return True
        else:
            return False
