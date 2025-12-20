# 🔒 Bloc bot_finalizer.py — verrouillage global des modules validés
import yaml

def finalize_bot(registry_path="config/module_registry.yaml"):
    with open(registry_path, "r") as f:
        registry = yaml.safe_load(f)

    count = 0
    for name, data in registry.items():
        if data["status"] == "actif" and isinstance(data["score"], (int, float)) and data["score"] >= 80:
            data["status"] = "verrouillé"
            data["replay"] = True
            data["export"] = True
            count += 1

    with open(registry_path, "w") as f:
        yaml.dump(registry, f)

    print(f"✅ {count} module(s) verrouillé(s) automatiquement.")

if __name__ == "__main__":
    finalize_bot()
