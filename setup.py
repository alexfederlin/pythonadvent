import os

# Dies ist der Inhalt für alle 24 Tage.
# Das Skript erstellt daraus automatisch die Ordner und Dateien.

calendar_data = {
    1: {
        "topic": "print()",
        "mission": """# 🎄 Tag 1: Der Weckruf

**Status:** 🔴 Kritisch  
**Ort:** Schlafzimmer des Weihnachtsmanns

Hallo Head of Digital Elves!

Hier spricht Oberelf Alabaster. Wir haben ein RIESIGES Problem. Der digitale Wecker des Weihnachtsmanns ist abgestürzt. Er schläft noch, dabei müssen wir in 24 Tagen starten!

Deine Aufgabe:
Repariere den Weck-Code. Wir müssen einen Text auf den Bildschirm schreiben, um ihn zu wecken.

Der Befehl dafür ist `print("Dein Text")`.

**Ziel:**
Schreibe ein Programm, das "Hallo Weihnachtsmann! Aufwachen!" ausgibt.
""",
        "code": """# 🎄 Tag 1: Der Weckruf
# Wir brauchen den Befehl print(), um Text anzuzeigen.
# Text muss immer in Anführungszeichen stehen: "Text"

# Schreibe hier deinen Code:
print("Hallo ...") 
"""
    },
    2: {
        "topic": "Variablen (Strings)",
        "mission": """# 🕯️ Tag 2: Das Namensschild

**Status:** 🟠 Wichtig  
**Ort:** Umkleidekabine

Guten Morgen! Der Chef ist wach (danke dir!), aber jetzt herrscht Chaos in der Umkleide. Die digitalen Namensschilder der Elfen sind gelöscht.

Deine Aufgabe:
Wir müssen Namen in sogenannten "Variablen" speichern. Eine Variable ist wie eine Kiste, auf der ein Etikett klebt.

Beispiel:
`name = "Alabaster"`

**Ziel:**
Erstelle eine Variable `elfen_name`, speichere einen Namen darin und gib ihn mit `print(elfen_name)` aus.
""",
        "code": """# 🕯️ Tag 2: Das Namensschild

# 1. Erstelle eine Variable mit dem Namen 'elfen_name'
# und weise ihr einen Namen in Anführungszeichen zu (z.B. "Glitzer").
# elfen_name = "..."

# 2. Gib die Variable aus. Wichtig: Hier KEINE Anführungszeichen beim print benutzen!
# print(...)
"""
    },
    3: {
        "topic": "Variablen (Integer)",
        "mission": """# 🕯️ Tag 3: Bestandsaufnahme

**Status:** 🟡 Routine  
**Ort:** Rentierstall

Gut gemacht mit den Namen! Jetzt müssen wir zählen. Rudolph und Co. stehen im Stall, aber der Computer zeigt "0" an.

Deine Aufgabe:
Wir brauchen Variablen für Zahlen. Zahlen schreibt man OHNE Anführungszeichen.

Beispiel:
`anzahl = 5`

**Ziel:**
Erstelle eine Variable `rentiere` mit dem Wert 9 und eine Variable `geschenke` mit dem Wert 0. Gib beide Zahlen aus.
""",
        "code": """# 🕯️ Tag 3: Bestandsaufnahme

# Wir brauchen Zahlen (Integer).
# Achtung: Zahlen schreibt man OHNE Gänsefüßchen!

# 1. Variable 'rentiere' auf 9 setzen


# 2. Variable 'geschenke' auf 0 setzen


# 3. Gib beide Variablen mit print() aus

"""
    },
    4: {
        "topic": "Rechnen",
        "mission": """# 🕯️ Tag 4: Futterberechnung

**Status:** 🟠 Hungrig  
**Ort:** Futterkammer

Die Rentiere haben Hunger! Ein Rentier frisst genau 2 magische Karotten pro Tag. Wir haben 9 Rentiere.

Deine Aufgabe:
Lass Python für dich rechnen. Der Computer ist ein super Taschenrechner.

Symbole:
`+` (Plus)
`-` (Minus)
`*` (Mal)
`/` (Geteilt)

**Ziel:**
Berechne `9 * 2` und gib das Ergebnis aus.
""",
        "code": """# 🕯️ Tag 4: Futterberechnung

rentiere = 9
karotten_pro_tier = 2

# Rechne die Gesamtmenge aus.
# Du kannst direkt im print rechnen: print(5 * 5)
# Oder eine neue Variable machen: gesamt = ... * ...

print("Wir brauchen so viele Karotten:")
# Hier rechnen:

"""
    },
    5: {
        "topic": "input()",
        "mission": """# 🕯️ Tag 5: Der Wunschzettel

**Status:** 🔴 Dringend  
**Ort:** Poststelle

Die Wunschzettel kommen rein! Aber unser System weiß nicht, was die Kinder wollen. Wir müssen das Programm interaktiv machen.

Deine Aufgabe:
Nutze `input()`, um dem Benutzer eine Frage zu stellen und die Antwort zu speichern.

Beispiel:
`wunsch = input("Was wünschst du dir? ")`

**Ziel:**
Frage nach einem Wunsch und gib danach aus: "Gespeichert: [Wunsch]"
""",
        "code": """# 🕯️ Tag 5: Der Wunschzettel

print("System bereit für Eingabe...")

# 1. Nutze input(), um den User zu fragen und speichere es in der Variable 'wunsch'
# wunsch = input("...hier Frage reinschreiben...")


# 2. Gib den gespeicherten Wunsch zur Bestätigung aus
print("Du wünschst dir:")
# print(wunsch)
"""
    },
    6: {
        "topic": "ASCII Art",
        "mission": """# 🎅 Tag 6: Nikolaus Spezial

**Status:** 🎉 Feierlich  
**Ort:** Wohnzimmer

Ho Ho Ho! Heute ist Nikolaus. Wir wollen eine Grafik auf den Bildschirm zaubern, aber wir haben nur Textzeichen.

Deine Aufgabe:
Male einen Stiefel oder einen Tannenbaum nur mit `print()` Befehlen und Zeichen wie `/`, `\`, `|`, `_` und `*`.

Das nennt man ASCII Art.

**Ziel:**
Zeichne etwas Weihnachtliches!
""",
        "code": """# 🎅 Tag 6: Nikolaus Spezial
# Zeichne mit print Befehlen ein Bild.
# Tipp: Du brauchst mehrere print Befehle untereinander.

# Beispiel für eine Spitze:
# print("   * ")
# print("  / \\  ")

# Jetzt du:


"""
    },
    7: {
        "topic": "if / else",
        "mission": """# 🕯️ Tag 7: Brav oder Frech?

**Status:** ⚖️ Heikel  
**Ort:** Das Große Buch

Wir müssen entscheiden, wer Geschenke bekommt. Dafür brauchen wir Logik!

Deine Aufgabe:
Nutze `if` (wenn) und `else` (sonst), um Entscheidungen zu treffen.

Beispiel:
```python
if zahl > 5:
    print("Groß")
else:
    print("Klein")
```

**Ziel:**
Erstelle eine Variable `artigkeit`. Wenn sie größer als 5 ist, gib "Geschenk!" aus. Sonst gib "Leider nur Kohle..." aus.
""",
        "code": """# 🕯️ Tag 7: Brav oder Frech?

artigkeit = 8  # Probier mal verschiedene Zahlen aus (1 bis 10)

# Schreibe hier die if-Abfrage:
# if artigkeit > 5:
    # print(...)  <- WICHTIG: Einrücken nicht vergessen! (Tab-Taste)
# else:
    # print(...)

"""
    },
    8: {
        "topic": "Boolean",
        "mission": """# 🕯️ Tag 8: Systemcheck

**Status:** 🛠️ Technisch  
**Ort:** Werkstatt

Bevor der Schlitten startet, müssen alle Lampen auf Grün stehen. In der Informatik gibt es dafür "Wahr" (`True`) und "Falsch" (`False`).

Deine Aufgabe:
Erstelle einen Schalter für den Schlitten.

**Ziel:**
Setze `schlitten_bereit = True`. Prüfe mit `if schlitten_bereit:`, ob wir starten können.
""",
        "code": """# 🕯️ Tag 8: Systemcheck

# True (Wahr) und False (Falsch) schreibt man groß.

schlitten_bereit = True

# Prüfe die Variable:
if schlitten_bereit:
    print("Motoren starten!")
else:
    print("Warten auf Wartung...")
"""
    },
    9: {
        "topic": "elif",
        "mission": """# 🕯️ Tag 9: Die Sortiermaschine

**Status:** 📦 Chaotisch  
**Ort:** Fließband

Die Geschenke purzeln durcheinander! Wir haben drei Kategorien: "Spielzeug", "Kleidung" und "Süßes".

Deine Aufgabe:
Nutze `elif` (else if - sonst wenn), um mehr als zwei Möglichkeiten zu prüfen.

**Ziel:**
Erstelle eine Variable `typ`.
Wenn "Spielzeug" -> Ab in Sack 1.
Wenn "Kleidung" -> Ab in Sack 2.
Sonst -> Ab in Sack 3.
""",
        "code": """# 🕯️ Tag 9: Die Sortiermaschine

typ = "Kleidung"  # Ändere das mal zu "Spielzeug" oder "Bonbon"

if typ == "Spielzeug":
    print("Kommt in den roten Sack.")
# Hier elif einfügen:
# elif typ == "Kleidung":
    # ...
else:
    print("Kommt in den blauen Sack.")
"""
    },
    10: {
        "topic": "String Methoden",
        "mission": """# 🕯️ Tag 10: GROSSBUCHSTABEN

**Status:** 👓 Unleserlich  
**Ort:** Poststelle

Oh nein! Die Adressaufkleber sind zu klein geschrieben. Die alten Elfen können das nicht lesen.

Deine Aufgabe:
Wandle Text in Großbuchstaben um. Dafür haben Text-Variablen eine eingebaute Funktion (Methode) namens `.upper()`.

**Ziel:**
Frage den Nutzer nach einem Wort und gib es in GROSSBUCHSTABEN wieder aus.
""",
        "code": """# 🕯️ Tag 10: GROSSBUCHSTABEN

wort = input("Gib ein Wort ein: ")

# Nutze .upper() um es groß zu machen
# gross = wort.upper()

print(gross)
"""
    },
    11: {
        "topic": "f-Strings",
        "mission": """# 🕯️ Tag 11: Der Adressaufkleber

**Status:** 🏷️ Wichtig  
**Ort:** Verpackung

Wir müssen schöne Sätze auf die Pakete drucken. Wir wollen Variablen direkt in den Text einbauen.

Das geht mit dem f-String: `f"Hallo {name}"`.

**Ziel:**
Definiere `name` und `stadt`. Gib den Satz aus: "Das Paket für [name] geht nach [stadt]."
""",
        "code": """# 🕯️ Tag 11: Der Adressaufkleber

name = "Lena"
stadt = "Berlin"

# Baue den Satz mit einem f-String (achte auf das f vor den Gänsefüßchen!)
satz = f"Das Paket für {name} geht nach ..."

print(satz)
"""
    },
    12: {
        "topic": "Bugfixing",
        "mission": """# 🕯️ Tag 12: Der tollpatschige Elf

**Status:** 💥 Fehlerhaft  
**Ort:** IT-Abteilung

Alarm! Elf Dussel hat Kaffee über die Tastatur gekippt. Sein Code funktioniert nicht mehr und wirft lauter rote Fehler.

Deine Aufgabe:
Sei ein Detektiv. Finde die 3 Fehler im Code und bringe ihn zum Laufen.

**Ziel:**
Das Programm muss fehlerfrei "Geschenke sind verpackt!" ausgeben.
""",
        "code": """# 🕯️ Tag 12: Bugfixing
# Hier sind 3 Fehler versteckt. Finde sie!
# Achte auf Klammern, Gänsefüßchen und Doppelpunkte.

status = "fertig"

if status == "fertig"
    print("Geschenke sind verpackt!)
else:
    print("Noch arbeiten...")
"""
    },
    13: {
        "topic": "Listen",
        "mission": """# 🕯️ Tag 13: Der Sack ist leer

**Status:** 📋 Leer  
**Ort:** Lagerhalle

Willkommen in Woche 3! Wir brauchen mehr Ordnung. Einzelne Variablen reichen nicht mehr, wir brauchen Listen.

Eine Liste schreibt man mit eckigen Klammern: `["A", "B", "C"]`.

**Ziel:**
Erstelle eine Liste namens `sack` mit 3 Geschenken darin. Gib die ganze Liste aus.
""",
        "code": """# 🕯️ Tag 13: Listen erstellen

# Erstelle eine Liste mit eckigen Klammern []
# sack = ["...", "...", "..."]

print("Im Sack ist:")
print(sack)
"""
    },
    14: {
        "topic": "Listen append",
        "mission": """# 🕯️ Tag 14: Nachzügler

**Status:** ➕ Hinzufügen  
**Ort:** Laderampe

Halt! Stopp! Ein Kind hat seinen Wunschzettel geändert. Wir müssen noch etwas in den Sack packen.

Deine Aufgabe:
Füge ein Element zu einer bestehenden Liste hinzu. Der Befehl ist `.append("Neues Ding")`.

**Ziel:**
Füge "Fahrrad" zu deiner Liste hinzu und gib sie erneut aus.
""",
        "code": """# 🕯️ Tag 14: Etwas hinzufügen

sack = ["Ball", "Puppe"]
print(f"Vorher: {sack}")

# Füge 'Fahrrad' hinzu:
# sack.append(...)

print(f"Nachher: {sack}")
"""
    },
    15: {
        "topic": "For-Loop",
        "mission": """# 🕯️ Tag 15: Geschenke verladen

**Status:** 🔄 Wiederholung  
**Ort:** Fließband

Der Sack ist zu schwer, um ihn auf einmal hochzuheben. Wir müssen jedes Geschenk einzeln scannen und verladen.

Deine Aufgabe:
Nutze eine `for`-Schleife, um jedes Element in der Liste einzeln anzuschauen.

```python
for geschenk in sack:
    print(geschenk)
```

**Ziel:**
Gib jedes Geschenk einzeln aus mit dem Text "Verladen: [Geschenk]".
""",
        "code": """# 🕯️ Tag 15: Schleifen (Loops)

sack = ["Auto", "Buch", "Kekse", "Socken"]

print("Starte Verladung...")

# Schreibe die for-Schleife:
# for ding in sack:
    # print(f"Verladen: {ding}")

print("Alles drin!")
"""
    },
    16: {
        "topic": "Time & Countdown",
        "mission": """# 🕯️ Tag 16: Der Countdown

**Status:** ⏱️ Zeitdruck  
**Ort:** Startbahn

Wir üben den Start! Dafür brauchen wir einen Countdown.
Wir brauchen das Modul `time`, um den Computer warten zu lassen.

Deine Aufgabe:
Zähle von 10 rückwärts bis 0.

**Ziel:**
Nutze eine Schleife (Tipp: `range(10, 0, -1)`) und `time.sleep(1)`, um runterzuzählen.
""",
        "code": """# 🕯️ Tag 16: Countdown
import time # Wir holen uns die Zeit-Funktion

print("Countdown gestartet!")

# range(start, stop, schritt)
# -1 bedeutet: wir zählen rückwärts
for zahl in range(10, 0, -1):
    print(zahl)
    # Hier 1 Sekunde warten:
    # time.sleep(1)

print("WROOOOM! Start!")
"""
    },
    17: {
        "topic": "Random",
        "mission": """# 🕯️ Tag 17: Die Schneeballschlacht

**Status:** ❄️ Spaß  
**Ort:** Innenhof

Mittagspause! Die Elfen machen eine Schneeballschlacht.
Wir brauchen einen Zufallsgenerator, um zu sehen, wer getroffen wird (Elf 1 bis Elf 6).

Deine Aufgabe:
Importiere `random` und nutze `random.randint(1, 6)`.

**Ziel:**
Simuliere einen Würfelwurf.
""",
        "code": """# 🕯️ Tag 17: Zufall
import random

print("Schneeball fliegt...")

# Erzeuge eine Zufallszahl zwischen 1 und 6
treffer = random.randint(1, 6)

print(f"Elf Nummer {treffer} wurde getroffen!")
"""
    },
    18: {
        "topic": "While Loop",
        "mission": """# 🕯️ Tag 18: Kekse essen

**Status:** 🍪 Lecker  
**Ort:** Küche

Der Weihnachtsmann muss zunehmen, damit der Anzug passt.
Solange er Hunger hat, muss er essen.

Deine Aufgabe:
Nutze eine `while`-Schleife. Sie läuft, so lange eine Bedingung wahr ist.

**Ziel:**
Setze `hunger = 5`. Solange `hunger > 0`: Iss einen Keks, ziehe 1 vom Hunger ab (`hunger = hunger - 1`).
""",
        "code": """# 🕯️ Tag 18: While Schleife (Solange...)

hunger = 5

while hunger > 0:
    print(f"Habe noch Hunger ({hunger})... Mampf!")
    # WICHTIG: Hunger muss weniger werden, sonst läuft die Schleife für immer!
    # hunger = hunger - 1

print("Pappsatt!")
"""
    },
    19: {
        "topic": "Funktionen",
        "mission": """# 🕯️ Tag 19: Der Verpackungs-Roboter

**Status:** 🤖 Automatisierung  
**Ort:** Werkstatt 2

Wir haben eine neue Maschine! Sie verpackt Dinge automatisch. Aber wir müssen sie programmieren.
Wenn wir Code oft brauchen, packen wir ihn in eine "Funktion".

**Ziel:**
Definiere eine Funktion `verpacken(gegenstand)`, die den Gegenstand mit Sternchen umrahmt ausdruckt.
""",
        "code": """# 🕯️ Tag 19: Funktionen definieren

# Hier bauen wir die Maschine (die Funktion):
def verpacken(gegenstand):
    print("****")
    print(f"*{gegenstand}*")
    print("****")

# Hier benutzen wir die Maschine:
verpacken("Puppe")
verpacken("Auto")
# Verpacke noch etwas:

"""
    },
    20: {
        "topic": "Return",
        "mission": """# 🕯️ Tag 20: Gewichtskontrolle

**Status:** ⚖️ Waage  
**Ort:** Laderampe

Der Schlitten darf nicht überladen werden!
Unsere Funktion muss uns das Gewicht zurückmelden, damit wir es zusammenrechnen können.

Deine Aufgabe:
Nutze `return`, um einen Wert aus der Funktion zurückzugeben.

**Ziel:**
Schreibe eine Funktion, die zwei Gewichte addiert und das Ergebnis zurückgibt.
""",
        "code": """# 🕯️ Tag 20: Rückgabewerte (Return)

def wiegen(paket1, paket2):
    gesamt = paket1 + paket2
    return gesamt  # Gib das Ergebnis zurück an das Hauptprogramm

# Wir rufen die Funktion auf und speichern das Ergebnis
gewicht = wiegen(5, 10)

print(f"Gesamtgewicht ist: {gewicht} kg")
"""
    },
    21: {
        "topic": "Dictionaries",
        "mission": """# 🕯️ Tag 21: Das Rentier-Navi

**Status:** 🗺️ Orientierung  
**Ort:** Schlitten-Cockpit

Listen sind gut, aber wir müssen wissen, WER WO steht. Dafür sind "Dictionaries" (Wörterbücher) perfekt.
Sie funktionieren wie Schlüssel und Wert: `{"Key": "Value"}`.

**Ziel:**
Erstelle ein Dictionary mit Rentier-Positionen: `{"Rudolph": "Vorne", "Dancer": "Mitte"}`.
""",
        "code": """# 🕯️ Tag 21: Dictionaries

# Geschweifte Klammern {} für Dictionaries
positionen = {
    "Rudolph": "Vorne",
    "Dancer": "Mitte",
    "Vixen": "Hinten"
}

# Wir greifen mit dem Namen (Key) auf den Wert zu:
wo_ist_rudi = positionen["Rudolph"]

print(f"Rudolph steht: {wo_ist_rudi}")
"""
    },
    22: {
        "topic": "Logik Kombinieren",
        "mission": """# 🕯️ Tag 22: Der Wetterbericht

**Status:** 🌨️ Wetter  
**Ort:** Wetterstation Nordpol

Wir brauchen eine Entscheidungshilfe für den Flug.
Wir kombinieren jetzt `random` und `if`.

**Ziel:**
Der Zufall entscheidet: 1 = Schneesturm, 0 = Klarer Himmel.
Wenn Schneesturm -> "Schneeketten anlegen!", Sonst -> "Abflugbereit!".
""",
        "code": """# 🕯️ Tag 22: Alles kombinieren
import random

wetter_code = random.randint(0, 1) # Zufall: 0 oder 1

print(f"Wetter-Code ist: {wetter_code}")

# Schreibe die If-Abfrage:
# Wenn 1 dann Schneeketten, sonst Gute Reise

"""
    },
    23: {
        "topic": "User Input Loop",
        "mission": """# 🕯️ Tag 23: Das Start-Passwort

**Status:** 🔒 Gesperrt  
**Ort:** Hangar Tor

Das Tor geht nur auf, wenn das geheime Passwort gesprochen wird.
Wir fragen den Nutzer so lange, bis es stimmt.

**Ziel:**
Setze das `passwort = "Zimtstern"`.
Mache eine `while`-Schleife: Solange die Eingabe NICHT das Passwort ist -> "Falsch, nochmal!".
""",
        "code": """# 🕯️ Tag 23: Passwort-Schutz

geheimnis = "Zimtstern"
eingabe = ""

# != bedeutet "nicht gleich"
while eingabe != geheimnis:
    eingabe = input("Wie lautet das Passwort? ")
    
    if eingabe == geheimnis:
        print("Zugriff erlaubt! Tor öffnet sich.")
    else:
        print("Zugriff verweigert!")
"""
    },
    24: {
        "topic": "Finale",
        "mission": """# 🎄 Tag 24: ABFLUG!

**Status:** ✨ Bereit  
**Ort:** Startbahn 1

Es ist soweit! Heiligabend!
Du hast das System repariert, die Rentiere gefüttert und den Schlitten beladen.

Deine Aufgabe:
Schreibe das finale Start-Programm.

1. Frage den Piloten (dich) nach dem Namen.
2. Starte einen kurzen Countdown (3...2...1).
3. Wünsche "Frohe Weihnachten [Name]"!

**DANKE, dass du Weihnachten gerettet hast!**
""",
        "code": """# 🎄 Tag 24: DAS FINALE
import time

print("Systeme fahren hoch...")

# 1. Input (Name)
pilot = input("Pilot, nenne deinen Namen: ")

print(f"Hallo Captain {pilot}. Startsequenz eingeleitet.")

# 2. Countdown (Loop)
for i in range(3, 0, -1):
    print(i)
    time.sleep(1)

# 3. Start!
print("🚀 WROOOOOM! Der Schlitten hebt ab!")
print("✨ Frohe Weihnachten! ✨")
print(f"Gute Reise, {pilot}!")
"""
    }
}

def create_calendar():
    base_dir = os.getcwd()
    print(f"Erstelle Adventskalender in {base_dir}...")

    for day, data in calendar_data.items():
        # Ordnername z.B. 01_Dezember
        folder_name = f"{day:02d}_Dezember"
        folder_path = os.path.join(base_dir, folder_name)

        # Ordner erstellen
        os.makedirs(folder_path, exist_ok=True)

        # mission.md schreiben
        with open(os.path.join(folder_path, "mission.md"), "w", encoding="utf-8") as f:
            f.write(data["mission"])

        # main.py schreiben
        with open(os.path.join(folder_path, "main.py"), "w", encoding="utf-8") as f:
            f.write(data["code"])
        
        print(f"✅ Tag {day} erstellt: {data['topic']}")

    print("\n🎄 Fertig! Lösche diese Datei jetzt am besten, damit nicht geschummelt wird! 😉")

if __name__ == "__main__":
    create_calendar()