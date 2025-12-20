# 📒 Automatisation de la génération du "registre comptable"
# --> Lié au Bouton “Générer registre comptable” dans bot_dashboard.py
def generate_ledger():
    import yaml

    ledger = [
        {
            "date": "2025-10-20",
            "version": "0.8.0",
            "action": "Initialisation du registre",
            "artefact": "module_registry.yaml",
            "validé_par": "Eric"
        },
        {
            "date": "2025-10-28",
            "version": "0.9.0",
            "action": "Ajout des release notes",
            "artefact": "bot_release_notes.md",
            "validé_par": "Eric"
        },
        {
            "date": "2025-11-01",
            "version": "1.0.0",
            "action": "Génération du contrat technique",
            "artefact": "bot_roadmap_contract.md",
            "validé_par": "Dr. Lemoine"
        },
        {
            "date": "2025-11-01",
            "version": "1.0.0",
            "action": "Archivage complet",
            "artefact": "release_1.0.0.zip",
            "validé_par": "Eric"
        },
        {
            "date": "2025-11-02",
            "version": "1.1.0",
            "action": "Prévision roadmap",
            "artefact": "bot_roadmap_forecast.yaml",
            "validé_par": "Eric"
        }
    ]

    with open("config/bot_registry_ledger.yaml", "w") as f:
        yaml.dump(ledger, f)

    print("✅ bot_registry_ledger.yaml généré.")
