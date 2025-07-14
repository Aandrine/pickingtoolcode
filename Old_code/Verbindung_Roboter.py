import customtkinter as ctk
from tkinter import messagebox


# Mock-Klasse für Robot
class MockRobot:
    def __init__(self, robot_model, host, port, ee_DO_type, ee_DO_num):
        self.robot_model = robot_model
        self.host = host
        self.port = port
        self.ee_DO_type = ee_DO_type
        self.ee_DO_num = ee_DO_num
        self.connected = False

    def connect(self):
        # Simuliert eine erfolgreiche Verbindung
        self.connected = True
        return {"success": True, "msg": f"Simulierte Verbindung zu {self.host}:{self.port} hergestellt"}

    def disconnect(self):
        # Simuliert das Trennen der Verbindung
        self.connected = False
        return {"success": True, "msg": "Simulierte Verbindung getrennt"}

    def setregister(self, cmd):
        if not self.connected:
            raise Exception("Roboter ist nicht verbunden.")
        return {"code": 0, "msg": f"Befehl '{cmd}' erfolgreich verarbeitet"}


# Funktion zur Herstellung der simulierten Verbindung
def connect_to_robot():
    try:
        # Mock-Roboter erstellen
        robot = MockRobot(
            robot_model="Fanuc",
            host="192.168.0.100",
            port=18735,
            ee_DO_type="RDO",
            ee_DO_num=7,
        )

        # Verbindung herstellen
        response = robot.connect()

        # Verbindungserfolg prüfen
        if response["success"]:
            update_scrollable_frame(f"Simulierte Verbindung erfolgreich: {response['msg']}", color="green")
        else:
            update_scrollable_frame(f"Simulierte Verbindung fehlgeschlagen: {response['msg']}", color="red")

        # Beispiel für das Senden eines Befehls
        cmd_response = robot.setregister("mock_command")
        if cmd_response["code"] == 0:
            update_scrollable_frame(f"Befehl erfolgreich: {cmd_response['msg']}", color="green")
        else:
            update_scrollable_frame(f"Befehl fehlgeschlagen: {cmd_response['msg']}", color="red")

        # Verbindung schließen
        disconnect_response = robot.disconnect()
        update_scrollable_frame(f"Verbindung geschlossen: {disconnect_response['msg']}", color="blue")
    except Exception as e:
        update_scrollable_frame(f"Ein Fehler ist aufgetreten: {str(e)}", color="red")


# Scrollbare Anzeige aktualisieren
def update_scrollable_frame(message: str, color: str = "black"):
    label = ctk.CTkLabel(master=scrollable_frame, text=message, text_color=color)
    label.pack(pady=5, padx=10)


# GUI erstellen
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("800x600")
root.title("Fanuc-Verbindung (Simulation)")

# Hauptcontainer
main_container = ctk.CTkFrame(master=root, height=80)
main_container.pack(fill="both", expand=True, padx=20, pady=20)

# Überschrift
title_label = ctk.CTkLabel(master=main_container, text="Fanuc-Verbindung (Simulation)", font=("Arial", 20))
title_label.pack(pady=20)

# Verbindungsbutton
connect_button = ctk.CTkButton(master=main_container, text="Simulierte Verbindung herstellen", command=connect_to_robot)
connect_button.pack(pady=20)

# Scrollbarer Frame für Statusmeldungen
scrollable_frame = ctk.CTkScrollableFrame(master=main_container, width=760, height=400)
scrollable_frame.pack(pady=20)

# Hauptfenster starten
root.mainloop()
