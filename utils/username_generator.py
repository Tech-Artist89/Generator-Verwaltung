from faker import Faker
import random

# Initialisiere Faker für die Option realistische Namen
fake = Faker()

# Erweiterte Gruppen für Konsonanten und Vokale
VOWELS = "aeiouy"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
FANTASY_SUFFIXES = ["ian", "ar", "on", "ius", "ara", "elle", "thas", "wen", "driel", "or", "iel", "nir", "orim"]
FANTASY_PREFIXES = ["El", "Tha", "Ara", "Da", "Gal", "Mor", "Xan", "Fen", "Vor", "Sar", "Rha"]

def generate_fantasy_name():
    """Generiert einen fantasievollen Namen mit abwechselnden Vokalen und Konsonanten und zusätzlichen Präfixen und Suffixen."""
    
    # Bestimme die Länge des Namens zufällig zwischen 3 und 8 Zeichen
    length = random.randint(3, 8)
    
    # Zufällig Präfix hinzufügen, falls es zur Länge passt
    name = random.choice(FANTASY_PREFIXES) if random.random() > 0.5 and length > 3 else ""
    remaining_length = length - len(name)

    # Beginnt mit einem zufälligen Großbuchstaben, abwechselnd Konsonant/Vokal
    if remaining_length > 0:
        name += random.choice(CONSONANTS).upper()
        for i in range(remaining_length - 1):
            if i % 2 == 0:
                name += random.choice(VOWELS)
            else:
                name += random.choice(CONSONANTS)

    # Optional doppelter Buchstabe
    if random.random() > 0.7 and len(name) < 8:
        name += random.choice(CONSONANTS) * 2  # Verdoppelt einen Konsonanten
    
    # Zufällig Suffix hinzufügen, falls es zur Länge passt
    if random.random() > 0.4 and len(name) < 8:
        suffix = random.choice(FANTASY_SUFFIXES)
        if len(name) + len(suffix) <= 8:
            name += suffix

    return name.capitalize()  # Nur der erste Buchstabe wird großgeschrieben

def generate_username(use_fantasy_names=False):
    """Generiert einen Benutzernamen im Format 'Vorname.Nachname'.
    
    use_fantasy_names: Falls True, wird ein fantasievoller Name generiert.
                       Falls False, wird ein realistischer Name generiert.
    """
    if use_fantasy_names:
        first_name = generate_fantasy_name()  # Fantasievoller Vorname mit 3-8 Zeichen
        last_name = generate_fantasy_name()   # Fantasievoller Nachname mit 3-8 Zeichen
    else:
        first_name = fake.first_name()  # Realistischer Vorname
        last_name = fake.last_name()    # Realistischer Nachname

    return f"{first_name}.{last_name}"
