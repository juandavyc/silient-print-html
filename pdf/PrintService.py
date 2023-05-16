import os

import win32api
import win32print


class PrintService:

    def __init__(self, _configuracion, scroll_text):
        # self.printers = [printer[2] for printer in win32print.EnumPrinters(2)]
        # 'C:\\belissaprinter\\GHOSTSCRIPT\\bin\\gswin32.exe'
        self.gscript = os.path.abspath(os.path.join("files","ghost","64","bin","gswin64.exe"))
        # 'C:\\belissaprinter\GSPRINT\\gsprint.exe'
        self.gsprint = os.path.abspath(os.path.join("files","gsprint","gsprint.exe"))
        # Canon MP250 series Printer
        self.printer = _configuracion['impresora']
        self.scroll_text = scroll_text

    def imprimir(self, ruta):

        self.scroll_text('Impresora -> Iniciando')

        print(ruta)
        # pdfFile = 'pdf1.pdf'

        win32api.ShellExecute(
            0,
            'open',
            self.gsprint,
            '-ghostscript "' + self.gscript + '" -printer "' + self.printer + '" ' + ruta,
            '.',
            0
        )

        #win32api.ShellExecute(0, "printto", ruta, f'"{self.printer}"', ".", 0)

        self.scroll_text('Impresora -> Terminado')

    # printer = win32print.GetDefaultPrinter()
