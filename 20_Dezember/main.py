# 🕯️ Tag 20: Rückgabewerte (Return)

def wiegen(paket1, paket2):
    gesamt = paket1 + paket2
    return gesamt  # Gib das Ergebnis zurück an das Hauptprogramm

# Wir rufen die Funktion auf und speichern das Ergebnis
gewicht = wiegen(5, 10)

print(f"Gesamtgewicht ist: {gewicht} kg")
