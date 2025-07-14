import socket

# Verbindungseinstellungen
ROBOT_IP = "192.168.0.100"
PORT = 18735


def connect_to_robot():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((ROBOT_IP, PORT))
        print(f"Verbindung zu {ROBOT_IP}:{PORT} hergestellt.")
        return client_socket
    except Exception as e:
        print(f"Fehler bei der Verbindung: {e}")
        return None


def send_command(socket, command):
    try:
        socket.sendall(command.encode('ascii'))
        print(f"Befehl gesendet: {command}")
    except Exception as e:
        print(f"Fehler beim Senden des Befehls: {e}")


def receive_response(socket):
    try:
        response = socket.recv(1024).decode('ascii')
        print(f"Answer from robot: {response}")
        return response
    except Exception as e:
        print(f"Error receiving response: {e}")
        return None


if __name__ == "__main__":
    robot_socket = connect_to_robot()

    if robot_socket:
        # Example: Send GETHOME command
        command = "GETHOME\n"
        send_command(robot_socket, command)

        # Antwort empfangen
        receive_response(robot_socket)

        # Verbindung schließen
        robot_socket.close()
