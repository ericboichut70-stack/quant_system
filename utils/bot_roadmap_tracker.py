# ✅ Bloc bot_roadmap_tracker.py — suivi automatique des étapes réalisées
import yaml

def track_roadmap(roadmap_path="config/bot_roadmap.yaml", registry_path="config/module_registry.yaml"):
    with open(roadmap_path, "r") as f:
        roadmap = yaml.safe_load(f)
    with open(registry_path, "r") as f:
        registry = yaml.safe_load(f)

    updated_steps = []
    new_steps = []
    for step in roadmap["étapes"]:
        label = step.replace("[x]", "").replace("[ ]", "").strip()
        if "verrouiller" in label:
            module = label.split("verrouiller")[-1].strip()
            if module in registry and registry[module]["status"] == "verrouillé":
                updated_steps.append(f"[x] {label}")
            else:
                new_steps.append(f"[ ] {label}")
        else:
            new_steps.append(step)

    roadmap["étapes"] = updated_steps + new_steps

    with open(roadmap_path, "w") as f:
        yaml.dump(roadmap, f)

    print(f"✅ Roadmap mise à jour avec {len(updated_steps)} étape(s) cochée(s).")

if __name__ == "__main__":
    track_roadmap()
