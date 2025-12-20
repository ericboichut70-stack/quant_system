# 📦 Bouton “Archiver les artefacts livrés” dans le dashboard
import yaml

def archive_artefacts(archive_path="config/bot_registry_archive.yaml"):
    new_entry = {
        "version": "1.0.0",
        "date": "2025-11-01",
        "artefacts": [
            "bot_certificate.md",
            "bot_roadmap_contract.md",
            "bot_roadmap_attestations.md",
            "bot_roadmap_signatures.yaml",
            "bot_roadmap_commitments.yaml",
            "bot_release_notes.md",
            "bot_manifest_final.yaml",
            "release_1.0.0.zip",
            "frozen_bot/v1_0_0"
        ]
    }

    try:
        with open(archive_path, "r") as f:
            archive = yaml.safe_load(f)
    except FileNotFoundError:
        archive = []

    archive.append(new_entry)

    with open(archive_path, "w") as f:
        yaml.dump(archive, f)

    print("✅ bot_registry_archive.yaml mis à jour.")
