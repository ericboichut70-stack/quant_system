# 🔊 Rapport vocal du contrat certifié
import streamlit as st
import pyttsx3

st.set_page_config(page_title="🔊 Contrat technique", layout="centered")
st.title("🔊 Synthèse vocale — Contrat de livraison")

summary = """
📑 Contrat technique — Version 1.0.0
Livré le 2025-11-01 par Eric.
Modules verrouillés : memory_evolution, auto_mentor_feedback, trend_detector.
Engagements respectés : score moyen ≥ 80, interface mentor opérationnelle, certificat généré.
Roadmap post-1.0.0 structurée, prochaine version prévue pour le 2025-12-01.
"""

st.text_area("📝 Synthèse vocale du contrat :", summary, height=250)

if st.button("🔊 Lire à voix haute"):
    engine = pyttsx3.init()
    engine.say(summary)
    engine.runAndWait()
    st.success("Lecture terminée.")
