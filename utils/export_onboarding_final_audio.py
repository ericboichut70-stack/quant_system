# 🔊 Résumé vocal final de l’onboarding complet
# 📌 Résultat : onboarding_final_summary.wav dans exports/audio/
import pyttsx3

def export_onboarding_final_audio(output_path="exports/audio/onboarding_final_summary.wav"):
    summary = """
Bienvenue dans Private Assistant.

Ce projet contient :
- Un registre des liens et raccourcis techniques
- Un index des scripts utilitaires
- Une cartographie interactive des artefacts
- Une documentation consolidée en markdown
- Des synthèses vocales pour l’onboarding et la navigation
- Un manifeste et une archive pour traçabilité complète

Tous les fichiers sont accessibles dans la page Synthèse Onboarding.
"""

    engine = pyttsx3.init()
    engine.save_to_file(summary, output_path)
    engine.runAndWait()
    print(f"✅ Résumé vocal final exporté : {output_path}")
