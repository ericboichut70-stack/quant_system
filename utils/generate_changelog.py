# 🧮 “Généation du changelog modulaire”
import yaml

def generate_changelog(output_path="config/bot_registry_changelog.yaml"):
    changelog = {
        "1.0.0": {
            "ajout": ["interface_mentor", "export_vocal_feedback"],
            "verrouillage": ["memory_evolution", "auto_mentor_feedback", "trend_detector"],
            "retrait": []
        },
        "0.9.0": {
            "ajout": ["trend_detector", "export_csv"],
            "correction": ["bug_import_module"],
            "retrait": []
        },
        "0.8.0": {
            "ajout": ["module_registry", "dashboard_pilotage"],
            "retrait": []
        }
    }

    with open(output_path, "w") as f:
        yaml.dump(changelog, f)

    print("✅ bot_registry_changelog.yaml généré.")
