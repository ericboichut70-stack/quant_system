# 🗺️ Génération de la cartographie des artefacts
import yaml

def generate_map(output_path="config/bot_registry_map.yaml"):
    map_data = {
        "bot_registry_manifest.yaml": {
            "contient": [
                "version",
                "modules_verrouillés",
                "certificats",
                "delta_comparaison",
                "scripts_index",
                "map_index"
            ]
        },
        "bot_registry_archive.yaml": {
            "contient": [
                "artefacts livrés",
                "release zip",
                "dossier gelé"
            ]
        },
        "bot_registry_scripts.yaml": {
            "référence": [
                "export_release_notes_json.py",
                "export_changelog_md.py",
                "export_certificates_md.py"
            ]
        },
        "bot_registry_certificates.yaml": {
            "indexe": [
                "certificats techniques",
                "artefacts validés",
                "scores mentor"
            ]
        },
        "bot_registry_delta.json": {
            "compare": [
                "ajouts",
                "retraits",
                "évolutions entre versions"
            ]
        },
        "bot_release_notes.json": {
            "journal": [
                "changements fonctionnels",
                "dates de livraison"
            ]
        }
    }

    with open(output_path, "w") as f:
        yaml.dump(map_data, f)

    print("✅ bot_registry_map.yaml généré.")
