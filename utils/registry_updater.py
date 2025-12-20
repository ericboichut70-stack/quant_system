# 🛠️ Script registry_updater.py — mise à jour automatique du registre
import os
import yaml

def update_registry(modules_path="modules", registry_path="config/module_registry.yaml"):
    registry = {}

    for f in sorted(os.listdir(modules_path)):
        if f.endswith(".py") and not f.startswith("__"):
            name = f[:-3]
            registry[name] = {
                "status": "actif",
                "score": "—",
                "replay": False,
                "export": True
            }

    with open(registry_path, "w") as f:
        yaml.dump(registry, f, sort_keys=False)

    print("✅ module_registry.yaml mis à jour.")

if __name__ == "__main__":
    update_registry()
