# 🔊 Rapport vocal de l’évolution des versions
import streamlit as st
import pyttsx3

st.set_page_config(page_title="🔊 Évolution des versions", layout="centered")
st.title("🔊 Synthèse vocale — Chronologie des livraisons")

summary = """
🕰️ Évolution des versions du bot :
Version 0.8.0 livrée le 20 octobre 2025 — modules de base et registre initial.
Version 0.9.0 livrée le 28 octobre 2025 — validations et release notes.
Version 1.0.0 livrée le 1er novembre 2025 — contrat, certificat, archive complète.
Version 1.1.0 prévue pour le 1er décembre 2025 — scoring communautaire et simulateur mentor.
"""

st.text_area("📝 Synthèse vocale de la timeline :", summary, height=300)

if st.button("🔊 Lire à voix haute"):
    engine = pyttsx3.init()
    engine.say(summary)
    engine.runAndWait()
    st.success("Lecture terminée.")
