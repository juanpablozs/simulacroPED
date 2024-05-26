# messaging.py
from datetime import datetime
import socket

class MensajeCliente:
    def __init__(self, server_address='127.0.0.1', server_port=16063):
        self.server_address = server_address
        self.server_port = server_port

    def enviar_mensaje(self, mensaje):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.server_address, self.server_port))
            s.sendall(mensaje.encode('utf-8'))
            return s.recv(1024).decode('utf-8')

def generate_response(message):
    if message == "FECHA":
        return datetime.now().strftime('%Y-%m-%d')
    elif message == "HORA":
        return datetime.now().strftime('%H:%M:%S')
    else:
        return "ERROR"
