# 🔊 Résumé vocal du manifeste pour onboarding contractuel
# 📌 Résultat : onboarding_manifest_summary.wav dans exports/audio/
import pyttsx3

def export_manifest_vocal(output_path="exports/audio/onboarding_manifest_summary.wav"):
    summary = """
Bienvenue dans le manifeste de Private Assistant.

Ce projet est structuré autour :
- D’un registre versionné des livrables
- D’un contrat d’engagements techniques
- D’un fichier de signatures validant chaque étape
- D’attestations de conformité et de validation mentor

Chaque bloc est consultable dans la page Manifeste Interactif et Contrats Projet.
"""

    engine = pyttsx3.init()
    engine.save_to_file(summary, output_path)
    engine.runAndWait()
    print(f"✅ Résumé vocal du manifeste exporté : {output_path}")
