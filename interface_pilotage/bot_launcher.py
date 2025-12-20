# 🚀 Script bot_launcher.py — unifié pour production et simulation
import argparse
import yaml

def launch_bot(mode, export, replay, registry_path="config/module_registry.yaml"):
    with open(registry_path, "r") as f:
        registry = yaml.safe_load(f)

    print(f"🚀 Lancement du bot en mode {mode}\n")
    for name, data in registry.items():
        if data["status"] == "verrouillé":
            print(f"✅ {name} | Score: {data['score']} | Export: {data['export']} | Replay: {data['replay']}")

    if export:
        print("📤 Export activé")
    if replay:
        print("🎞️ Replay activé")

    print("\n🎯 Bot lancé avec modules validés.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="🎮 Lancement du bot Private Assistant")
    parser.add_argument("--mode", choices=["simulation", "production"], default="simulation")
    parser.add_argument("--export", action="store_true")
    parser.add_argument("--replay", action="store_true")
    args = parser.parse_args()

    launch_bot(args.mode, args.export, args.replay)
