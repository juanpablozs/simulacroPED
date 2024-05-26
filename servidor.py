# servidor.py
import socket
from mensajes import generate_response

def start_server():
    server_address = '127.0.0.1'
    server_port = 16063

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((server_address, server_port))
        server.listen()
        print(f"Servidor escuchando en {server_address}:{server_port}")

        while True:
            client_socket, addr = server.accept()
            handle_client(client_socket)

def handle_client(client_socket):
    with client_socket:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            response = generate_response(message)
            client_socket.sendall(response.encode('utf-8'))

if __name__ == "__main__":
    start_server()
