# 🚀 Script bot_deployer.py — lancement en mode mentorat ou production
import argparse
import yaml

def deploy_bot(mode, registry_path="config/module_registry.yaml"):
    with open(registry_path, "r") as f:
        registry = yaml.safe_load(f)

    locked = [name for name, data in registry.items() if data["status"] == "verrouillé"]
    print(f"🚀 Déploiement du bot en mode {mode}\n")
    for name in locked:
        print(f"✅ Module activé : {name} — Score {registry[name]['score']}")

    if mode == "mentorat":
        print("\n🧑‍🏫 Interface mentor activée")
    else:
        print("\n🎯 Mode production activé")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="🚀 Déploiement du bot")
    parser.add_argument("--mode", choices=["production", "mentorat"], default="production")
    args = parser.parse_args()

    deploy_bot(args.mode)
