# 🔒 final_validator.py — verrouillage automatique après test
import yaml

def lock_module(module_name, score, registry_path="config/module_registry.yaml"):
    with open(registry_path, "r") as f:
        registry = yaml.safe_load(f)

    if module_name in registry:
        registry[module_name]["status"] = "verrouillé"
        registry[module_name]["score"] = score
        registry[module_name]["replay"] = True
        registry[module_name]["export"] = True

        with open(registry_path, "w") as f:
            yaml.dump(registry, f, sort_keys=False)

        print(f"✅ Module verrouillé : {module_name}")
    else:
        print(f"❌ Module introuvable : {module_name}")

if __name__ == "__main__":
    lock_module("auto_mentor_feedback", 85)
