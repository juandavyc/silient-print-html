import os
import signal
import sys
import tkinter as tk
from tkinter import messagebox

from belissa.Model import Model
from belissa.View import View


class Controller:
    CONTADOR_LIMITE = 100

    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def main(self):
        self._asignar_elementos()
        self._configuracion_basica()
        self.model.main()
        self.view.main()
        os.kill(os.getpid(), signal.SIGTERM)

    def _asignar_elementos(self):
        # Asingar informe logs
        self.model.scroll_insert(self.scroll_insert_text)
        self.model.socket_insert(self.view.socket_estado)

    def on_button_click(self):
        self.model.main()


    def scroll_insert_text(self, text):
        self.view.tab_principal_scroll.config(state='normal')
        self.view.tab_principal_scroll.insert(tk.END, f'{self.model.get_date_time()} : {text}\n')
        self.view.tab_principal_scroll.yview(tk.END)
        self.view.tab_principal_scroll.config(state='disabled')

        estado = self.model.limpiar_scroll_text()
        if estado:
            self.view.tab_principal_scroll.delete('1.0', tk.END)

    def _configuracion_basica(self):
        self.view.ip_value.set(self.model._data_configuracion['ip'])
        self.view.puerto_value.set(self.model._data_configuracion['puerto'])
        self.view.impresora_value.set(self.model._data_configuracion['impresora'])
        self.view.calidad_value.set(self.model._data_configuracion['calidad'].replace('\n', '[**]'))

    def guardar_configuracion(self):

        self.model._data_configuracion['ip'] = self.view.ip_value.get()
        self.model._data_configuracion['puerto'] = self.view.puerto_value.get()
        self.model._data_configuracion['impresora'] = self.view.impresora_value.get()
        self.model._data_configuracion['calidad'] = self.view.calidad_value.get().replace('[**]', '\n')

        if self.model.guardar_configuracion():
            messagebox.showinfo('Bien', 'Configuracion Guardada, inicie de nuevo el programa.')
            os.kill(os.getpid(), signal.SIGTERM)
        else:
            messagebox.showerror('Bien', 'Error al Guardar la Configuración')
