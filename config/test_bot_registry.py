# ✅ Test de vérification croisée — Private Assistant Registry

import os

# 📁 Dossiers à vérifier
folders = {
    "documentation_md": [
        "bot_registry_manifest_final_closure.md",
        "bot_registry_manifest_lancement_circuit.md",
        "bot_registry_banner_cloture_officielle.md",
        "bot_registry_banner_lancement_circuit.md",
        "bot_registry_banner_index_manifest_final.md"
    ],
    "config": [
        "onboarding_final_project_summary.txt",
        "onboarding_manifest_synthese_finale.txt",
        "onboarding_index_manifest_final.txt",
        "onboarding_manifest_final_closure.txt",
        "onboarding_manifest_lancement_circuit.txt",
        "onboarding_final_project_summary.mp3",
        "onboarding_manifest_synthese_finale.mp3",
        "onboarding_index_manifest_final.mp3",
        "onboarding_manifest_final_closure.mp3",
        "onboarding_manifest_lancement_circuit.mp3"
    ],
    "assets": [
        "banner_synthese_finale.png",
        "banner_cloture_officielle.png",
        "banner_lancement_circuit.png",
        "banner_index_manifest_final.png"
    ],
    "pages": [
        "36_🔊_Synthèse_Finale.py",
        "37_🔊_Manifeste_Synthèse_Finale.py",
        "38_🔊_Index_Manifest_Final.py",
        "39_🔊_Clôture_Officielle.py",
        "40_🚀_Lancement_Circuit.py"
    ]
}

# ✅ Vérification
def verify_registry():
    print("🔍 Vérification croisée des artefacts du bot...")
    for folder, files in folders.items():
        print(f"\n📁 Dossier : {folder}")
        for file in files:
            path = os.path.join(folder, file)
            if os.path.exists(path):
                print(f"✅ Présent : {file}")
            else:
                print(f"❌ Manquant : {file}")

if __name__ == "__main__":
    verify_registry()
