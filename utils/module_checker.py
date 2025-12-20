# 🛠️ Script module_checker.py — pour lister les modules disponibles
import os

def list_modules(path="modules"):
    print("📦 Modules disponibles :\n")
    for f in sorted(os.listdir(path)):
        if f.endswith(".py") and not f.startswith("__"):
            print(f" - {f[:-3]}")

if __name__ == "__main__":
    list_modules()

# Possible à lancer avec: python utils/module_checker.py
