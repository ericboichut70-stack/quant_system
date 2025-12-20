# Possible à appeler depuis une interface CLI ou Streamlit pour afficher les replays par module.
# modules/replay_generator.py

def generate_replay_summary(module_name, replay_path):
    try:
        with open(replay_path, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        return f"❌ Replay introuvable pour {module_name}"

    summary = f"📘 Replay — {module_name}\n"
    for line in lines:
        summary += f"• {line.strip()}\n"

    return summary
