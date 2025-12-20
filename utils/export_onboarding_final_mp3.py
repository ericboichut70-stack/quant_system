# 🎧 Générer une version .mp3 de la synthèse finale
# 📌 Résultat : onboarding_final_summary.mp3 dans exports/audio/
import pyttsx3
from pydub import AudioSegment

def export_onboarding_final_mp3(output_path="exports/audio/onboarding_final_summary.mp3"):
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

    temp_wav = "exports/audio/temp_final.wav"
    engine = pyttsx3.init()
    engine.save_to_file(summary, temp_wav)
    engine.runAndWait()

    sound = AudioSegment.from_wav(temp_wav)
    sound.export(output_path, format="mp3")
    print(f"✅ Audio MP3 exporté : {output_path}")
