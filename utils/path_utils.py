# utils/path_utils.py
import sys
import os

def get_resource_path(relative_path):
    """Gibt den absoluten Pfad zu eingebetteten Ressourcen zurück, auch wenn das Programm als .exe ausgeführt wird."""
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, relative_path)

# Beispiel: Hintergrundbild und .qss-Datei laden
image_path = get_resource_path("assets/images/passwort-generator.jpg")
qss_path = get_resource_path("assets/styles.qss")