# 🖥️ Interface CLI — lancement avec options
import argparse
from activation_protocol import launch_bot

parser = argparse.ArgumentParser(description="🎮 Lancement du bot Private Assistant")
parser.add_argument("--mode", choices=["simulation", "production"], default="simulation", help="Mode de lancement")
parser.add_argument("--export", action="store_true", help="Activer l’export")
parser.add_argument("--replay", action="store_true", help="Activer les replays")

args = parser.parse_args()

print(f"🚀 Lancement en mode {args.mode}")
if args.export:
    print("📤 Export activé")
if args.replay:
    print("🎞️ Replay activé")

launch_bot()

# Exemple d’utilisation :
python interface_pilotage/cli_launcher.py --mode production --export --replay
