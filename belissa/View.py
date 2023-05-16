import tkinter as tk
from tkinter import ttk, scrolledtext


class View(tk.Tk):

    def __init__(self, controller):
        super().__init__()

        self.controller = controller
        self._logo_belissa = tk.PhotoImage(file='files/images/logo.gif')
        self.socket_estado = tk.StringVar()

        self.socket_estado.set('Belissa.socket : sin_estado')
        self.title('Belissa Print Service v1.0')
        self.geometry('600x400')
        self.eval('tk::PlaceWindow . center')

        self._establecer_estilo()
        self._crear_ventana_principal()
        self._crear_tabs()

    def _establecer_estilo(self):
        s = ttk.Style()

        s.configure(
            'Custom.TFrame',
            background='#F9F9F9',
        )
        s.configure(
            'Belissa.TNotebook',
            background='#E9EEF4',
        )
        s.configure(
            'BelissaNotebookFrame.TFrame',
            background='#F9F9F9',
        )
        s.configure(
            'Belissa.TLabel',
            background='#F9F9F9',
            foreground='#314D62'
        )
        self.config(bg='#EAEFF5')

    def _crear_ventana_principal(self):
        label_logo = tk.Label(
            self,
            image=self._logo_belissa,
            highlightbackground="#EAEFF6",
            bd=0,
            text='xxx'
        )
        self.label_estado = ttk.Label(self, textvariable=self.socket_estado)
        self.main_frm = ttk.Frame(self)

        label_logo.grid(row=0, column=0)
        self.label_estado.grid(row=1, column=0)
        self.main_frm.grid(row=2, column=0, padx=20, pady=20)

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=2)

        self.columnconfigure(0, weight=1)

    def _componentes_tab_principal(self, tabulador):
        tab_principal_label = ttk.Label(tabulador, text='Log: ', style='Belissa.TLabel')
        self.tab_principal_scroll = scrolledtext.ScrolledText(
            tabulador, wrap=tk.WORD, font="Arial 10",
            height=100, bg='#FAFCFF', fg='#335066'
        )
        self.tab_principal_scroll.insert(tk.END, f'Bienvenido a Belissa\n')
        self.tab_principal_scroll.config(state='disabled')

        tab_principal_label.grid(row=0, column=0, padx=5, pady=5, sticky="WN")
        self.tab_principal_scroll.grid(row=0, column=1, padx=5, pady=5)

        tabulador.columnconfigure(0, weight=0)
        tabulador.columnconfigure(1, weight=2)
        tabulador.rowconfigure(0, weight=1)

    def _componentes_tab_configurar(self, tabulador):
        self.ip_value = tk.StringVar()
        tab_configurar_label_ip = ttk.Label(tabulador, text='Direccion IP  ', style='Belissa.TLabel')
        tab_configurar_entry_ip = ttk.Entry(tabulador, width=80, textvariable=self.ip_value)

        self.puerto_value = tk.StringVar()
        tab_configurar_label_puerto = ttk.Label(tabulador, text='Puerto IP ', style='Belissa.TLabel')
        tab_configurar_entry_puerto = ttk.Entry(tabulador, width=80, textvariable=self.puerto_value)

        self.impresora_value = tk.StringVar()
        tab_configurar_label_impresora = ttk.Label(tabulador, text='Impresora ', style='Belissa.TLabel')
        tab_configurar_entry_impresora = ttk.Entry(tabulador, width=80, textvariable=self.impresora_value)

        self.calidad_value = tk.StringVar()
        tab_configurar_label_calidad = ttk.Label(tabulador, text='Calidad [**]', style='Belissa.TLabel')
        tab_configurar_entry_calidad = ttk.Entry(tabulador, width=80, textvariable=self.calidad_value)

        tab_configurar_button_guardar = ttk.Button(
            tabulador, text='Guardar configuracion',
            command=self.controller.guardar_configuracion,

        )  # command=enviar

        tab_configurar_label_ip.grid(row=0, column=0, padx=5, pady=5, sticky='W')
        tab_configurar_entry_ip.grid(row=0, column=1, padx=5, pady=5)

        tab_configurar_label_puerto.grid(row=1, column=0, padx=5, pady=5, sticky='W')
        tab_configurar_entry_puerto.grid(row=1, column=1, padx=5, pady=5)

        tab_configurar_label_impresora.grid(row=2, column=0, padx=5, pady=5, sticky='W')
        tab_configurar_entry_impresora.grid(row=2, column=1, padx=5, pady=5)

        tab_configurar_label_calidad.grid(row=3, column=0, padx=5, pady=5, sticky='W')
        tab_configurar_entry_calidad.grid(row=3, column=1, padx=5, pady=5)

        tab_configurar_button_guardar.grid(row=4, columnspan=2, padx=5, pady=5)

        tabulador.columnconfigure(0, weight=0)
        tabulador.columnconfigure(1, weight=2)
        tabulador.columnconfigure(2, weight=2)
        tabulador.columnconfigure(3, weight=2)

    def _crear_tabs(self):
        control_tabulador = ttk.Notebook(self.main_frm, style="Belissa.TNotebook")
        tab_principal = ttk.Frame(control_tabulador, style="BelissaNotebookFrame.TFrame")
        tab_configurar = ttk.Frame(control_tabulador, style="BelissaNotebookFrame.TFrame")

        control_tabulador.add(tab_principal, text='Principal', padding=15)
        control_tabulador.add(tab_configurar, text='Configurar', padding=15)

        control_tabulador.pack()

        self._componentes_tab_principal(tab_principal)
        self._componentes_tab_configurar(tab_configurar)

        # control_tabulador.select(1)

    def main(self):
        self.mainloop()
