import socket

# Verbindungsdetails
ROBOT_IP = "192.168.0.100"
ROBOT_PORT = 60008  # Port, auf dem der Roboter lauscht

def test_connection():
    try:
        # Socket erstellen
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)  # Timeout für die Verbindung
            print(f"Verbinde zu {ROBOT_IP}:{ROBOT_PORT}...")
            s.connect((ROBOT_IP, ROBOT_PORT))
            print("Verbindung erfolgreich!")

            # Testbefehl senden
            test_message = "TEST MESSAGE\n"  # Beispielbefehl
            s.sendall(test_message.encode('utf-8'))
            print(f"Gesendet: {test_message.strip()}")

            # Antwort empfangen
            response = s.recv(1024).decode('utf-8')
            print(f"Antwort erhalten: {response}")
    except socket.timeout:
        print("Verbindung fehlgeschlagen: Timeout.")
    except ConnectionRefusedError:
        print("Verbindung fehlgeschlagen: Ziel verweigert die Verbindung.")
    except Exception as e:
        print(f"Fehler: {e}")

# Test starten
test_connection()
