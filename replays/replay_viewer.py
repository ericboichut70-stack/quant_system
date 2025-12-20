# Lecture des replays
# 🔁 2. Script replay_viewer.py — Lecture des sessions
# Ce script affiche les replays générés pour audit ou relecture pédagogique.
# replay_viewer.py
import os

REPLAY_DIR = "replays"

def list_replays():
    files = [f for f in os.listdir(REPLAY_DIR) if f.endswith(".txt") or f.endswith(".md")]
    return files

def view_replay(file_name):
    path = os.path.join(REPLAY_DIR, file_name)
    if not os.path.exists(path):
        print("Fichier introuvable.")
        return
    with open(path, "r") as f:
        print(f"\n--- {file_name} ---\n")
        print(f.read())

if __name__ == "__main__":
    files = list_replays()
    print("📂 Replays disponibles :")
    for i, f in enumerate(files):
        print(f"{i+1}. {f}")
    
    choice = input("Choisir un numéro de replay à afficher : ")
    try:
        index = int(choice) - 1
        view_replay(files[index])
    except:
        print("Choix invalide.")
