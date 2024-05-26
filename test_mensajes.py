# test_messaging.py
import unittest
import subprocess
import time
import socket
from datetime import datetime
from mensajes import MensajeCliente

class TestMessaging(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Iniciar el servidor en un subproceso
        cls.server_process = subprocess.Popen(['python3', 'servidor.py'])
        time.sleep(1)  # Esperar un poco para asegurar que el servidor se inicie

    @classmethod
    def tearDownClass(cls):
        # Terminar el servidor
        cls.server_process.terminate()
        cls.server_process.wait()

    def setUp(self):
        self.cliente = MensajeCliente()

    def test_fecha(self):
        response = self.cliente.enviar_mensaje("FECHA")
        self.assertEqual(response, datetime.now().strftime('%Y-%m-%d'))

    def test_hora(self):
        response = self.cliente.enviar_mensaje("HORA")
        self.assertEqual(response, datetime.now().strftime('%H:%M:%S'))

    def test_error(self):
        response = self.cliente.enviar_mensaje("SALUDO")
        self.assertEqual(response, "ERROR")

    def test_conexion(self):
        # Intentar conectarse al servidor para verificar que está funcionando
        try:
            with socket.create_connection(('127.0.0.1', 16063), timeout=2) as s:
                connected = True
        except (ConnectionRefusedError, socket.timeout):
            connected = False
        self.assertTrue(connected, "El servidor no está aceptando conexiones")

if __name__ == '__main__':
    unittest.main()
