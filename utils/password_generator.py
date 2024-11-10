# utils/password_generator.py
import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special=True):
    # Aufbau des Passworts: Ein Zeichen pro aktivierter Kategorie sicherstellen
    password = []

    # Immer mindestens ein Kleinbuchstabe, da Kleinbuchstaben standardmäßig enthalten sind
    password.append(random.choice(string.ascii_lowercase))

    # Falls Großbuchstaben erwünscht sind, einen Großbuchstaben hinzufügen
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))

    # Falls Zahlen erwünscht sind, eine Zahl hinzufügen
    if use_numbers:
        password.append(random.choice(string.digits))

    # Falls Sonderzeichen erwünscht sind, ein Sonderzeichen hinzufügen
    if use_special:
        password.append(random.choice("!@#$%^&*"))

    # Restliche Länge berechnen
    remaining_length = length - len(password)
    
    # Kombinierter Zeichensatz für restliche Zeichen
    characters = string.ascii_lowercase  # Kleinbuchstaben sind immer enthalten
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += "!@#$%^&*"

    # Restliche Zeichen zufällig auswählen und zum Passwort hinzufügen
    password.extend(random.choice(characters) for _ in range(remaining_length))

    # Passwort zufällig durchmischen
    random.shuffle(password)

    # Liste in einen String konvertieren und zurückgeben
    return ''.join(password)
