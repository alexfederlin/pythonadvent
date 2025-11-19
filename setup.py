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

**Erklärung:**
Der Befehl `print(...)` ist wie ein Drucker. Er schreibt das, was in den Klammern steht, auf den Bildschirm.
Damit der Computer weiß, wo der Text anfängt und aufhört, müssen wir ihn in Anführungszeichen `"..."` packen.

**Ziel:**
Schreibe ein Programm, das "Hallo Weihnachtsmann! Aufwachen!" ausgibt.
""",
        "code": """# 🎄 Tag 1: Der Weckruf

# Wir brauchen den Befehl print(), um Text anzuzeigen.
# Denke daran: Text muss immer in Anführungszeichen "..." stehen.

# Aufgabe: Schreibe einen print-Befehl, der "Hallo Weihnachtsmann! Aufwachen!" ausgibt.

"""
    },
    2: {
        "topic": "Variablen (Strings)",
        "mission": """# 🕯️ Tag 2: Das Namensschild

**Status:** 🟠 Wichtig  
**Ort:** Umkleidekabine

Guten Morgen! Der Chef ist wach (danke dir!), aber jetzt herrscht Chaos in der Umkleide. Die digitalen Namensschilder der Elfen sind gelöscht.

Deine Aufgabe:
Wir müssen Namen in sogenannten "Variablen" speichern.

**Erklärung:**
Stell dir eine Variable wie einen Karton vor.
1. Du schreibst einen Namen auf den Karton (z.B. `elfen_name`).
2. Du legst einen Inhalt hinein (z.B. `"Alabaster"`).
3. Das Gleichzeichen `=` packt den Inhalt in den Karton.

Beispiel:
`name = "Alabaster"`

**Ziel:**
Erstelle eine Variable `elfen_name`, speichere einen Namen darin und gib ihn mit `print(elfen_name)` aus.
""",
        "code": """# 🕯️ Tag 2: Das Namensschild

# 1. Erstelle eine Variable mit dem Namen 'elfen_name'.
#    Speichere darin einen Namen (in Anführungszeichen, z.B. "Glitzer").
#    Tipp: variable = "Wert"


# 2. Gib den Inhalt der Variable auf dem Bildschirm aus.
#    Nutze dafür den print() Befehl mit dem Variablennamen.
#    WICHTIG: Hier KEINE Anführungszeichen, sonst druckt er nur das Wort "elfen_name" statt des Inhalts!

"""
    },
    3: {
        "topic": "Variablen (Integer)",
        "mission": """# 🕯️ Tag 3: Bestandsaufnahme

**Status:** 🟡 Routine  
**Ort:** Rentierstall

Gut gemacht mit den Namen! Jetzt müssen wir zählen. Rudolph und Co. stehen im Stall, aber der Computer zeigt "0" an.

Deine Aufgabe:
Wir brauchen Variablen für Zahlen (Integer).

**Erklärung:**
Computer unterscheiden zwischen Text ("Strings") und Zahlen ("Integer").
* Text braucht Gänsefüßchen: `"Hallo"`
* Zahlen stehen nackt da: `5` (Wenn du `"5"` schreibst, denkt der Computer, es ist ein Wort und kann nicht damit rechnen!)

**Ziel:**
Erstelle eine Variable `rentiere` mit dem Wert 9 und eine Variable `geschenke` mit dem Wert 0. Gib beide Zahlen aus.
""",
        "code": """# 🕯️ Tag 3: Bestandsaufnahme

# Wir brauchen Zahlen (Integer).
# Achtung: Zahlen schreibt man im Code OHNE Gänsefüßchen!

# 1. Erstelle eine Variable 'rentiere' und setze sie auf 9.


# 2. Erstelle eine Variable 'geschenke' und setze sie auf 0.


# 3. Gib beide Variablen mit print() aus.
#    (Erinnerung an Tag 2: Variable in die Klammer, ohne Anführungszeichen)

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

print("Wir brauchen so viele Karotten:")

# Aufgabe:
# Rechne die Gesamtmenge aus (Rentiere mal Karotten pro Tier).
# Du kannst das Ergebnis direkt in den print-Befehl schreiben
# ODER erst in einer neuen Variable 'gesamt' speichern und diese dann drucken.


"""
    },
    5: {
        "topic": "input()",
        "mission": """# 🕯️ Tag 5: Der Wunschzettel

**Status:** 🔴 Dringend  
**Ort:** Poststelle

Die Wunschzettel kommen rein! Aber unser System weiß nicht, was die Kinder wollen. Wir müssen das Programm interaktiv machen.

**Erklärung:**
Bisher hat der Computer nur geredet (`print`). Jetzt soll er zuhören!
Der Befehl `input()` hält das Programm an und wartet, bis der Mensch etwas tippt und ENTER drückt.

Beispiel:
`antwort = input("Wie heißt du? ")`
Hier wird die Frage angezeigt und das, was man tippt, landet in der Variable `antwort`.

**Ziel:**
Frage nach einem Wunsch und gib danach aus: "Gespeichert: [Wunsch]"
""",
        "code": """# 🕯️ Tag 5: Der Wunschzettel

print("System bereit für Eingabe...")

# 1. Nutze input(), um den User zu fragen und speichere das Ergebnis in der Variable 'wunsch'.
#    Schreibe deine Frage als Text in die Klammern von input("...").


# 2. Gib den gespeicherten Wunsch zur Bestätigung aus.
print("Du wünschst dir:")
#    Gib hier (wie an Tag 2) den Inhalt der Variable 'wunsch' aus.

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

# Aufgabe: Zeichne ein Bild mit print Befehlen.
# Du brauchst mehrere print Befehle untereinander.

# Kleines Beispiel für eine Spitze:
# print("   * ")
# print("  / \\  ")

# Jetzt bist du dran - tob dich aus!


"""
    },
    7: {
        "topic": "if / else",
        "mission": """# 🕯️ Tag 7: Brav oder Frech?

**Status:** ⚖️ Heikel  
**Ort:** Das Große Buch

Wir müssen entscheiden, wer Geschenke bekommt. Dafür brauchen wir Logik!

**Erklärung:**
Das Zauberwort heißt `if` (wenn). Damit kann der Computer Entscheidungen treffen.
Wichtig sind zwei Dinge:
1. Der Doppelpunkt `:` am Ende der Zeile.
2. Das "Einrücken" (Lücke am Anfang der nächsten Zeile). Das zeigt dem Computer, was genau passieren soll, *wenn* die Bedingung stimmt.

Beispiel:
```python
if zahl > 5:
    print("Groß") # Das hier passiert nur, wenn zahl > 5 ist
else:
    print("Klein") # Das passiert sonst
```

**Ziel:**
Erstelle eine Variable `artigkeit`. Wenn sie größer als 5 ist, gib "Geschenk!" aus. Sonst gib "Leider nur Kohle..." aus.
""",
        "code": """# 🕯️ Tag 7: Brav oder Frech?

artigkeit = 8  # Ändere diese Zahl später zum Testen (z.B. auf 2)

# Schreibe hier die if-Abfrage:
# Prüfe: Ist artigkeit größer als (>) 5?

    # Wenn ja: Gib "Geschenk!" aus (Denk an die Einrückung! Drücke die Tab-Taste)

# else:

    # Sonst: Gib "Kohle..." aus

"""
    },
    8: {
        "topic": "Boolean",
        "mission": """# 🕯️ Tag 8: Systemcheck

**Status:** 🛠️ Technisch  
**Ort:** Werkstatt

Bevor der Schlitten startet, müssen alle Lampen auf Grün stehen.

**Erklärung:**
In der Informatik gibt es einen Datentyp, der nur zwei Zustände kennt:
* `True` (Wahr / An / Ja)
* `False` (Falsch / Aus / Nein)

Das nennt man "Boolean". Das Praktische ist: Eine `if`-Abfrage prüft *immer*, ob etwas `True` ist.
Statt `if licht_an == True:` können Profis einfach `if licht_an:` schreiben.

**Ziel:**
Setze `schlitten_bereit = True`. Prüfe mit `if schlitten_bereit:`, ob wir starten können.
""",
        "code": """# 🕯️ Tag 8: Systemcheck

# 1. Erstelle eine Variable 'schlitten_bereit' und setze sie auf True.
#    Achtung: True schreibt man groß!


# 2. Schreibe eine if-Abfrage, die prüft ob der Schlitten bereit ist.
#    Profi-Tipp: Du brauchst kein "== True". Schreib einfach: if schlitten_bereit:

    # Wenn bereit: Gib "Motoren starten!" aus.

    # Sonst (else): Gib "Warten..." aus.
"""
    },
    9: {
        "topic": "elif",
        "mission": """# 🕯️ Tag 9: Die Sortiermaschine

**Status:** 📦 Chaotisch  
**Ort:** Fließband

Die Geschenke purzeln durcheinander! Wir haben drei Kategorien: "Spielzeug", "Kleidung" und "Süßes".

**Erklärung:**
Wenn wir mehr als zwei Optionen haben (nicht nur Ja/Nein), reicht `if` und `else` nicht.
Dafür gibt es `elif`. Das ist kurz für "else if" (sonst wenn).

Der Computer prüft von oben nach unten:
1. `if`... (Trifft das zu? Wenn ja, fertig.)
2. `elif`... (Wenn das erste nicht zutraf: Trifft das hier zu?)
3. `else`... (Wenn gar nichts zutraf.)

**Ziel:**
Erstelle eine Variable `typ`.
Wenn "Spielzeug" -> Ab in Sack 1.
Wenn "Kleidung" -> Ab in Sack 2.
Sonst -> Ab in Sack 3.
""",
        "code": """# 🕯️ Tag 9: Die Sortiermaschine

typ = "Kleidung"  # Teste später auch "Spielzeug" oder "Bonbon"

if typ == "Spielzeug":
    print("Kommt in den roten Sack.")

# Aufgabe: Füge hier die Prüfung für "Kleidung" ein.
# Nutze dafür den Befehl: elif ...:
    # Gib dann aus "Kommt in den blauen Sack."


else:
    print("Kommt in den Rest-Sack.")
"""
    },
    10: {
        "topic": "String Methoden",
        "mission": """# 🕯️ Tag 10: GROSSBUCHSTABEN

**Status:** 👓 Unleserlich  
**Ort:** Poststelle

Oh nein! Die Adressaufkleber sind zu klein geschrieben. Die alten Elfen können das nicht lesen.

**Erklärung:**
Python gibt uns Werkzeuge für Text (Strings).
Diese Werkzeuge hängen wir mit einem Punkt `.` an die Variable an.
`.upper()` macht alles GROSS.
`.lower()` macht alles klein.

Beispiel:
`name = "Tim"`
`grosser_name = name.upper()` -> "TIM"

**Ziel:**
Frage den Nutzer nach einem Wort und gib es in GROSSBUCHSTABEN wieder aus.
""",
        "code": """# 🕯️ Tag 10: GROSSBUCHSTABEN

wort = input("Gib ein Wort ein: ")

# Aufgabe:
# 1. Wende .upper() auf die Variable 'wort' an.
# 2. Speichere das Ergebnis in einer neuen Variable (z.B. 'gross').


# 3. Gib die neue Variable aus.

"""
    },
    11: {
        "topic": "f-Strings",
        "mission": """# 🕯️ Tag 11: Der Adressaufkleber

**Status:** 🏷️ Wichtig  
**Ort:** Verpackung

Wir müssen schöne Sätze auf die Pakete drucken. Wir wollen Variablen direkt in den Text einbauen.

**Erklärung:**
Das ist ein super wichtiges Werkzeug: Der **f-String**.
Das `f` steht für "format". Es erlaubt uns, Variablen direkt in einen Satz zu schmuggeln, indem wir sie in geschweifte Klammern `{}` setzen.

Ohne f-String (umständlich): `print("Hallo " + name)`
Mit f-String (cool): `print(f"Hallo {name}")`

Vergiss das kleine `f` vor den Gänsefüßchen nicht!

**Ziel:**
Definiere `name` und `stadt`. Gib den Satz aus: "Das Paket für [name] geht nach [stadt]."
""",
        "code": """# 🕯️ Tag 11: Der Adressaufkleber

name = "Lena"
stadt = "Berlin"

# Aufgabe:
# Baue den Satz "Das Paket für ... geht nach ..." mit einem f-String.
# 1. Schreibe ein f vor den String: f"..."
# 2. Setze die Variablen name und stadt in geschweifte Klammern {} an die richtige Stelle.

satz = ...

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
# Hier sind 3 Fehler versteckt.
# Achte genau auf:
# - Klammern ()
# - Anführungszeichen "
# - Doppelpunkte : bei if-Abfragen (Erinnerst du dich an Tag 7?)

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

Willkommen in Woche 3! Wir brauchen mehr Ordnung. Einzelne Variablen reichen nicht mehr.

**Erklärung:**
Eine **Liste** ist eine Variable, die mehrere Dinge gleichzeitig speichern kann.
Man erkennt sie an den **eckigen Klammern** `[]`.

Beispiel:
`einkaufsliste = ["Milch", "Eier", "Mehl"]`

**Ziel:**
Erstelle eine Liste namens `sack` mit 3 Geschenken darin. Gib die ganze Liste aus.
""",
        "code": """# 🕯️ Tag 13: Listen erstellen

# Aufgabe:
# 1. Erstelle eine Liste 'sack'.
# 2. Schreibe 3 Geschenke (als Text in Anführungszeichen) hinein, getrennt mit Kommas.
#    Tipp: sack = ["...", "...", "..."]


print("Im Sack ist:")
# 3. Gib die Liste aus (einfach print(sack) )

"""
    },
    14: {
        "topic": "Listen append",
        "mission": """# 🕯️ Tag 14: Nachzügler

**Status:** ➕ Hinzufügen  
**Ort:** Laderampe

Halt! Stopp! Ein Kind hat seinen Wunschzettel geändert. Wir müssen noch etwas in den Sack packen.

**Erklärung:**
Listen sind veränderbar! Mit dem Befehl `.append()` (anhängen) können wir etwas Neues ans Ende der Liste kleben.

Beispiel:
`liste.append("Neues")`

**Ziel:**
Füge "Fahrrad" zu deiner Liste hinzu und gib sie erneut aus.
""",
        "code": """# 🕯️ Tag 14: Etwas hinzufügen

sack = ["Ball", "Puppe"]

# (Erinnerung an Tag 11: Das hier unten ist ein f-String mit den {} Klammern!)
print(f"Vorher: {sack}")

# Aufgabe:
# Nutze den Befehl .append(...), um "Fahrrad" in den Sack zu packen.
# Der Befehl gehört zur Variable: sack.append(...)


print(f"Nachher: {sack}")
"""
    },
    15: {
        "topic": "For-Loop",
        "mission": """# 🕯️ Tag 15: Geschenke verladen

**Status:** 🔄 Wiederholung  
**Ort:** Fließband

Der Sack ist zu schwer, um ihn auf einmal hochzuheben. Wir müssen jedes Geschenk einzeln scannen und verladen.

**Erklärung:**
Die **For-Schleife** (Loop) ist eines der mächtigsten Werkzeuge. Sie geht eine Liste Element für Element durch.

```python
for ding in sack:
    print(ding)
```
Das bedeutet: "Nimm das erste Ding aus dem Sack, nenne es `ding`, und mach was damit. Dann nimm das nächste..."

**Ziel:**
Gib jedes Geschenk einzeln aus mit dem Text "Verladen: [Geschenk]".
""",
        "code": """# 🕯️ Tag 15: Schleifen (Loops)

sack = ["Auto", "Buch", "Kekse", "Socken"]

print("Starte Verladung...")

# Aufgabe: Schreibe eine for-Schleife.
# Sie soll jedes 'ding' im 'sack' durchgehen.

# for ... in ...:
    # Gib in der Schleife aus: "Verladen: {ding}"
    # (Erinnerung an Tag 11: Nutze dafür einen f-String!)
    

print("Alles drin!")
"""
    },
    16: {
        "topic": "Time & Countdown",
        "mission": """# 🕯️ Tag 16: Der Countdown

**Status:** ⏱️ Zeitdruck  
**Ort:** Startbahn

Wir üben den Start! Dafür brauchen wir einen Countdown.

**Erklärung:**
Manchmal kann Python nicht alles alleine. Wir müssen ein "Modul" importieren.
`import time` lädt Funktionen für die Uhrzeit.
`time.sleep(1)` lässt den Computer für 1 Sekunde schlafen (warten).

Außerdem nutzen wir `range(Start, Ende, Schritt)`.
`range(10, 0, -1)` zählt von 10 bis 1 in Einerschritten rückwärts.

**Ziel:**
Nutze eine Schleife und `time.sleep(1)`, um runterzuzählen.
""",
        "code": """# 🕯️ Tag 16: Countdown
import time # Wir holen uns die Zeit-Funktion

print("Countdown gestartet!")

# Aufgabe:
# Schreibe eine for-Schleife mit range().
# Start: 10, Ende: 0, Schritt: -1 (rückwärts).
# Nenne die Zähl-Variable z.B. 'zahl'.
# (Erinnerung an Tag 15: for zahl in ...:)

# for ... 
    # 1. Gib die Zahl aus
    
    # 2. Warte eine Sekunde mit time.sleep(1)


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

**Erklärung:**
Wir brauchen wieder ein Modul: `import random` (Zufall).
Der Befehl `random.randint(1, 6)` würfelt eine Zahl zwischen 1 und 6.

**Ziel:**
Simuliere einen Würfelwurf.
""",
        "code": """# 🕯️ Tag 17: Zufall
import random

print("Schneeball fliegt...")

# Aufgabe:
# Erzeuge eine Zufallszahl zwischen 1 und 6 mit random.randint(..., ...)
# Speichere sie in der Variable 'treffer'.


# (Erinnerung an Tag 11: Hier benutzen wir wieder den f-String für die Ausgabe)
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

**Erklärung:**
Die **While-Schleife** läuft nicht eine feste Anzahl mal (wie `for`), sondern **solange** eine Bedingung wahr ist.
`while hunger > 0:` bedeutet: "Solange der Hunger größer als 0 ist, mach weiter..."

WICHTIG: In der Schleife muss sich der Hunger ändern, sonst hört sie nie auf!

**Ziel:**
Setze `hunger = 5`. Solange `hunger > 0`: Iss einen Keks, ziehe 1 vom Hunger ab (`hunger = hunger - 1`).
""",
        "code": """# 🕯️ Tag 18: While Schleife (Solange...)

hunger = 5

# Aufgabe: Schreibe den Kopf der while-Schleife.
# Solange hunger größer als 0 ist...
# while ...:

    # (Erinnerung an Tag 11: f-String!)
    print(f"Habe noch Hunger ({hunger})... Mampf!")
    
    # WICHTIG: Ziehe hier 1 vom Hunger ab!
    # hunger = ...

print("Pappsatt!")
"""
    },
    19: {
        "topic": "Funktionen",
        "mission": """# 🕯️ Tag 19: Der Verpackungs-Roboter

**Status:** 🤖 Automatisierung  
**Ort:** Werkstatt 2

Wir haben eine neue Maschine! Sie verpackt Dinge automatisch.

**Erklärung:**
Wenn wir Code oft brauchen, packen wir ihn in eine **Funktion**. Das ist wie ein eigenes kleines Unterprogramm.
Man erkennt es am Wort `def` (definieren).
Was in den Klammern steht (z.B. `gegenstand`), ist der Input für die Maschine.

**Ziel:**
Definiere eine Funktion `verpacken(gegenstand)`, die den Gegenstand mit Sternchen umrahmt ausdruckt.
""",
        "code": """# 🕯️ Tag 19: Funktionen definieren

# Hier bauen wir die Maschine (die Funktion).
# Ergänze den Code in der Funktion.

def verpacken(gegenstand):
    print("****")
    # Aufgabe: Gib den Gegenstand aus, am besten mit Sternchen davor und dahinter
    # z.B. * Puppe *
    # (Tipp: Nutze dafür wieder einen f-String: f"*{...}*")
    
    print("****")

# Hier testen wir die Maschine.
# Rufe die Funktion auf mit verschiedenen Dingen.
verpacken("Puppe")
# Rufe sie noch einmal auf mit "Auto":

"""
    },
    20: {
        "topic": "Return",
        "mission": """# 🕯️ Tag 20: Gewichtskontrolle

**Status:** ⚖️ Waage  
**Ort:** Laderampe

Der Schlitten darf nicht überladen werden!

**Erklärung:**
Bisher haben unsere Funktionen nur etwas gedruckt.
Manchmal soll eine Funktion aber etwas **ausrechnen und zurückgeben**, damit wir mit dem Ergebnis weiterrechnen können.
Dafür gibt es den Befehl `return` (zurückgeben).

Wenn `return` kommt, ist die Funktion fertig und wirft das Ergebnis heraus.

**Ziel:**
Schreibe eine Funktion, die zwei Gewichte addiert und das Ergebnis zurückgibt.
""",
        "code": """# 🕯️ Tag 20: Rückgabewerte (Return)

def wiegen(paket1, paket2):
    gesamt = paket1 + paket2
    # Aufgabe: Gib das Ergebnis 'gesamt' an das Hauptprogramm zurück.
    # Nutze den Befehl: return ...


# Hier nutzen wir deine Funktion:
# Wir speichern das, was zurück kommt (return), in der Variable 'gewicht'
gewicht = wiegen(5, 10)

print(f"Gesamtgewicht ist: {gewicht} kg")
"""
    },
    21: {
        "topic": "Dictionaries",
        "mission": """# 🕯️ Tag 21: Das Rentier-Navi

**Status:** 🗺️ Orientierung  
**Ort:** Schlitten-Cockpit

Listen (`[]`) sind gut für Aufzählungen. Aber wenn wir Dinge nachschlagen wollen, brauchen wir ein **Dictionary** (Wörterbuch).

**Erklärung:**
Ein Dictionary nutzt geschweifte Klammern `{}`.
Es besteht immer aus Paaren: `Schlüssel : Wert`.
`telefonbuch = {"Mama": "12345", "Papa": "67890"}`

Wenn ich wissen will, welche Nummer Mama hat, frage ich: `telefonbuch["Mama"]`.

**Ziel:**
Erstelle ein Dictionary mit Rentier-Positionen: `{"Rudolph": "Vorne", "Dancer": "Mitte"}`.
""",
        "code": """# 🕯️ Tag 21: Dictionaries

# Das hier ist ein Dictionary (Wörterbuch) mit geschweiften Klammern {}:
positionen = {
    "Rudolph": "Vorne",
    "Dancer": "Mitte",
    "Vixen": "Hinten"
}

# Aufgabe: Finde heraus, wo Rudolph steht.
# Hole dir den Wert aus dem Dictionary, indem du den Namen ("Rudolph") in eckigen Klammern dahinter schreibst.

# wo_ist_rudi = positionen[...]

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
# (Erinnerung an Tag 11: f-String!)
print(f"Wetter-Code ist: {wetter_code}")

# Aufgabe: Schreibe eine Logik für den Piloten.
# 1. Wenn (if) wetter_code gleich 1 ist:
#    Drucke "Achtung: Schneeketten anlegen!"

# 2. Sonst (else):
#    Drucke "Freie Fahrt! Abflugbereit."

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

# Aufgabe: Schreibe die while-Schleife.
# Solange 'eingabe' NICHT GLEICH 'geheimnis' ist...
# (Erinnerung an Tag 18: while ...:)

# while ... != ...:
    
    # Frage den User nach dem Passwort (input) und speichere es in 'eingabe'
    
    # (Optional) Wenn du willst, kannst du prüfen:
    # Wenn eingabe richtig -> "Offen!"
    # Sonst -> "Falsch!"

print("Zugriff erlaubt! Tor öffnet sich.")
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

# Aufgabe 1: Frage nach dem Namen des Piloten und speichere ihn in 'pilot' (input).


# (Erinnerung an Tag 11: f-String für den Namen!)
print(f"Hallo Captain {pilot}. Startsequenz eingeleitet.")

# Aufgabe 2: Schreibe einen Countdown von 3 bis 1.
# (Erinnerung an Tag 16: for ... in range(...): )
# Vergiss nicht das time.sleep(1) zwischen den Zahlen!


# Aufgabe 3: Gib den finalen Start-Befehl und "Frohe Weihnachten" aus!

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