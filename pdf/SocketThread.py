import ssl
import pathlib
import asyncio
import json
import threading
from tkinter import messagebox

import websockets


class SocketThread(threading.Thread):
    USERS = set()
    VALUE = 0
    VALUE = 0

    def __init__(self, _configuracion, pdf_crear, socket_estado, scroll_text):
        threading.Thread.__init__(self)

        self.pdf_crear = pdf_crear
        self.scroll_text = scroll_text
        self.socket_estado = socket_estado
        self.ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        self.ssl_context.load_cert_chain('files/pem/mycert.pem', keyfile='files/pem/mykey.key')
        # No modificar
        self._configuracion = _configuracion

    def run(self):
        asyncio.run(self.star_socket())

    def users_event(self):
        return json.dumps({"type": "users", "count": len(self.USERS)})

    def value_event(self):
        return json.dumps({"type": "value", "value": self.VALUE})

    def rtm_event(self, placa):
        return json.dumps({"type": "value", "value": f'Información RTM recibida - {placa}'})

    async def _websocket(self, websocket):

        self.scroll_text('Socket -> Usuario conectado')

        try:

            self.USERS.add(websocket)
            websockets.broadcast(self.USERS, self.users_event())

            self.socket_estado.set(f'( {len(self.USERS)} ) usuario(s) conectado(s)')

            await websocket.send(self.value_event())
            async for message in websocket:
                event = json.loads(message)
                if event["action"] == "print":
                    self.scroll_text(f"Socket -> Información RTM recibida {event['rtm']['placa']}")
                    # Crear PDF
                    self.pdf_crear(event["rtm"])
                    # Notificar a usuarios
                    websockets.broadcast(self.USERS, self.rtm_event(event['rtm']['placa']))

                else:

                    self.scroll_text(f"Socket -> Evento no soportado")
        finally:
            self.USERS.remove(websocket)
            websockets.broadcast(self.USERS, self.users_event())

    async def star_socket(self):
        try:

            async with websockets.serve(
                    self._websocket,
                    self._configuracion['ip'],
                    self._configuracion['puerto'],
                   # ssl=self.ssl_context
            ):
                self.socket_estado.set('Socket : Iniciado')
                await asyncio.Future()  # run forever

        except:
            messagebox.showerror('Error gravemente malo fatal OMG',
                                 f'Algo pasa con el Socket, contacte a soporte técnico inmediatamente!!!\nBelissa: AYUDAAAAAAAAA')

            self.socket_estado.set('Socket : no_iniciado_ERROR')
