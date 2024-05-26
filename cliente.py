# cliente.py
from mensajes import MensajeCliente

def main():
    server_address = input("Ingrese la dirección del servidor (default: 127.0.0.1): ") or '127.0.0.1'
    cliente = MensajeCliente(server_address=server_address)

    messages = ["FECHA", "HORA", "SALUDO"]

    for message in messages:
        response = cliente.enviar_mensaje(message)
        print(f"Respuesta del servidor: {response}")

if __name__ == "__main__":
    main()
