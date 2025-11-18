# 🎄 Tag 24: DAS FINALE
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
