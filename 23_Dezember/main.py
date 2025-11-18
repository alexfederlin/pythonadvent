# 🕯️ Tag 23: Passwort-Schutz

geheimnis = "Zimtstern"
eingabe = ""

# != bedeutet "nicht gleich"
while eingabe != geheimnis:
    eingabe = input("Wie lautet das Passwort? ")
    
    if eingabe == geheimnis:
        print("Zugriff erlaubt! Tor öffnet sich.")
    else:
        print("Zugriff verweigert!")
