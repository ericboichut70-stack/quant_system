# 🔊 Synthèse vocale “Clôture officielle” avec date et version
# 📌 Résultat : onboarding_cloture_summary.wav dans exports/audio/
import pyttsx3
from datetime import datetime

def export_cloture_vocal(output_path="exports/audio/onboarding_cloture_summary.wav"):
    now = datetime.now().strftime("%d %B %Y à %Hh%M")
    version = "1.0.0"

    summary = f"""
Clôture officielle du projet Private Assistant.

Version : {version}
Date : {now}

Tous les blocs ont été validés, archivés et soumis :
- Manifeste versionné
- Contrats et attestations
- Synthèses vocales
- Certification finale
- Archive complète

Le projet est verrouillé et prêt pour diffusion.
"""

    engine = pyttsx3.init()
    engine.save_to_file(summary, output_path)
    engine.runAndWait()
    print(f"✅ Synthèse vocale de clôture exportée : {output_path}")
