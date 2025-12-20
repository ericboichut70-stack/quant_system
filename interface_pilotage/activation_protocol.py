# 🚀 Bloc activation_protocol.py — lancement du bot en production
import yaml

def launch_bot(registry_path="config/module_registry.yaml"):
    with open(registry_path, "r") as f:
        registry = yaml.safe_load(f)

    print("🚀 Lancement du bot — modules verrouillés\n")
    for name, data in registry.items():
        if data["status"] == "verrouillé":
            print(f"✅ {name} | Score: {data['score']} | Export: {data['export']} | Replay: {data['replay']}")

    print("\n🎯 Bot activé avec modules validés.")

if __name__ == "__main__":
    launch_bot()

# 🧠 Ajout automatique dans bot_log.md à chaque lancement
# Puis appelle log_activation (mode, export, replay) à la fin du script.
from datetime import datetime

def log_activation(mode, export, replay, registry_path="config/module_registry.yaml", log_path="replays/bot_log.md"):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(registry_path, "r") as f:
        registry = yaml.safe_load(f)

    locked = [name for name, data in registry.items() if data["status"] == "verrouillé"]

    with open(log_path, "a") as f:
        f.write(f"\n## Activation — {now}\n")
        f.write(f"- Mode : {mode}\n- Export : {export}\n- Replay : {replay}\n")
        f.write(f"- Modules activés : {', '.join(locked) if locked else 'Aucun'}\n")
