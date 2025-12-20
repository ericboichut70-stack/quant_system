# 🔊 Synthèse vocale “version publique” pour diffusion externe
# 📌 Résultat : onboarding_public_summary.wav dans exports/audio/
import pyttsx3

def export_public_vocal(output_path="exports/audio/onboarding_public_summary.wav"):
    summary = """
Bienvenue dans la version publique du projet Private Assistant.

Ce projet propose :
- Une documentation claire et consolidée
- Des synthèses vocales pour l’onboarding
- Un manifeste versionné et validé
- Une archive complète pour audit et diffusion

Tous les fichiers publics sont listés dans le registre de diffusion.
"""

    engine = pyttsx3.init()
    engine.save_to_file(summary, output_path)
    engine.runAndWait()
    print(f"✅ Synthèse vocale publique exportée : {output_path}")
