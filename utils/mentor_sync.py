# 🔄 Script mentor_sync.py — fusion des commentaires dans le registre
import yaml

def sync_mentor_feedback(feedback_path="config/mentor_feedback.yaml", registry_path="config/module_registry.yaml"):
    with open(feedback_path, "r") as f:
        feedback = yaml.safe_load(f)

    with open(registry_path, "r") as f:
        registry = yaml.safe_load(f)

    updated = 0
    for name, data in feedback.items():
        if name in registry:
            registry[name]["score"] = data["score"]
            registry[name]["mentor_comment"] = data["mentor_comment"]
            updated += 1

    with open(registry_path, "w") as f:
        yaml.dump(registry, f)

    print(f"✅ {updated} module(s) mis à jour avec feedback mentor.")

if __name__ == "__main__":
    sync_mentor_feedback()
