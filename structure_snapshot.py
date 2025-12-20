# 📁 Structure actuelle — script pour photo à l’instant T
# A lancer dans powershell avec python structure_snapshot.py
import os

def snapshot_structure(root=".", indent=0):
    for item in sorted(os.listdir(root)):
        path = os.path.join(root, item)
        prefix = "│   " * indent + ("├── " if os.path.isdir(path) else "    ")
        print(f"{prefix}{item}")
        if os.path.isdir(path):
            snapshot_structure(path, indent + 1)

if __name__ == "__main__":
    print("📸 Structure actuelle de TRADING_BOT\n")
    snapshot_structure(".")
