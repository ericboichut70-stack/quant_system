# 🧪 Script replay_viewer.py multi-module
import os

REPLAY_DIR = "replays"

def view_all_replays():
    print("\n📂 Relecture multi-module — Replays disponibles\n")
    files = [f for f in os.listdir(REPLAY_DIR) if f.endswith(".txt") or f.endswith(".md")]

    for f in files:
        print(f"\n--- {f} ---")
        with open(os.path.join(REPLAY_DIR, f), "r") as file:
            print(file.read())

if __name__ == "__main__":
    view_all_replays()
