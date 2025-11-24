import os
import shutil
import subprocess

# KONFIGURATION
SOURCE_DIR = "." 
# Das ist der Ordner, in den wir das Repo des Kindes gecloned haben
TARGET_DIR = "../adventskalender2025"

def run_git_command(command, cwd, ignore_error=False):
    try:
        # check=True wirft einen Fehler bei Problemen
        subprocess.run(command, shell=True, check=True, cwd=cwd)
    except subprocess.CalledProcessError as e:
        if not ignore_error:
            print(f"⚠️ Git Info: '{command}' lieferte Exit-Code {e.returncode}.")
        return False
    return True

def publish(day):
    folder_name = f"{day:02d}_Dezember"
    source = os.path.join(SOURCE_DIR, folder_name)
    target = os.path.join(TARGET_DIR, folder_name)

    # 1. Prüfen, ob das Ziel-Repo überhaupt da ist
    if not os.path.exists(TARGET_DIR):
        print(f"❌ Fehler: Ordner '{TARGET_DIR}' nicht gefunden.")
        print(f"   Bitte führe erst aus: git clone <URL-DES-KIND-REPOS> {TARGET_DIR}")
        return

    # 2. AUTOMATISCHER GIT PULL
    # Wir ignorieren Fehler hier, weil ein leeres Repo beim ersten Pull immer meckert.
    print("📡 Hole aktuellen Stand vom Kind-Repo...")
    run_git_command("git pull", cwd=TARGET_DIR, ignore_error=True)

    # 3. Quellen prüfen
    if not os.path.exists(source):
        print(f"❌ Fehler: Quelle {source} nicht gefunden. Hast du setup_calendar.py ausgeführt?")
        return
    
    # 4. Kopieren
    if os.path.exists(target):
        shutil.rmtree(target)
    shutil.copytree(source, target)
    print(f"✅ Dateien für Tag {day} kopiert.")

    # 5. Spezialfall Tag 1: Speicher-Skript
    if day == 1:
        shutil.copy("speichern.py", os.path.join(TARGET_DIR, "speichern.py"))
        print("✅ speichern.py wurde übertragen.")

    # 6. Git Operationen (Robustere Logik)
    print("⚙️ Bereite Upload vor...")
    
    # Add und Commit
    run_git_command("git add .", cwd=TARGET_DIR)
    
    # Wir versuchen zu committen. Wenn "nichts zu tun ist", ist das auch okay.
    # Wir prüfen hier nicht strikt auf True/False, damit der Push danach trotzdem läuft.
    run_git_command(f'git commit -m "Mission Tag {day} freigeschaltet"', cwd=TARGET_DIR, ignore_error=True)

    # IMMER Pushen (Das ist neu: Der Push passiert jetzt unabhängig vom Commit-Erfolg)
    print("🚀 Pushe zum Kind-Repo...")
    if run_git_command("git push", cwd=TARGET_DIR):
        print("✨ Erledigt! Die Mission ist online.")
    else:
        print("❌ Upload fehlgeschlagen. Hast du 'gh auth login' gemacht?")

if __name__ == "__main__":
    try:
        tag_input = input("Welchen Tag freischalten? (1-24): ")
        if tag_input.strip():
            tag = int(tag_input)
            publish(tag)
        else:
            print("Keine Eingabe.")
    except ValueError:
        print("Bitte eine Zahl eingeben!")