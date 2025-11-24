import os
import subprocess
import time

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        print("⚠️ Hmmm, das hat nicht ganz geklappt.")
        return False
    return True

print("💾 Mission wird gespeichert...")
time.sleep(1)

# 1. Alles vormerken
run_command("git add .")

# 2. Speichern mit Zeitstempel
zeit = time.strftime("%H:%M:%S")
nachricht = f"Fortschritt gespeichert um {zeit}"

if run_command(f'git commit -m "{nachricht}"'):
    print("✅ Deine Arbeit wurde sicher im Tresor verstaut!")
    
    # 3. Optional: Gleich hochladen, damit du es auch sehen kannst
    print("🚀 Sende Daten an das Hauptquartier...")
    if run_command("git push"):
        print("✅ Upload erfolgreich!")
    else:
        print("⚠️ Upload ging nicht, aber lokal ist es gespeichert.")
else:
    print("ℹ️ Nichts Neues zu speichern.")

print("\nDu bist bereit für die nächste Mission!")
time.sleep(2)