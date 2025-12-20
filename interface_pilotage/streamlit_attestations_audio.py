# 🔊 Rapport vocal des attestations certifiées
import streamlit as st
import pyttsx3

st.set_page_config(page_title="🔊 Attestations certifiées", layout="centered")
st.title("🔊 Synthèse vocale — Attestations officielles")

summary = """
📑 Attestations officielles — Version 1.0.0
Mentor principal : Dr. Lemoine, score 95.
Commentaire : Livraison conforme, modules verrouillés avec rigueur.
Mentor secondaire : A. Dupont, score 88.
Commentaire : Interface mentor bien pensée.
Validation communautaire prévue pour version 1.1.0.
"""

st.text_area("📝 Synthèse vocale des attestations :", summary, height=250)

if st.button("🔊 Lire à voix haute"):
    engine = pyttsx3.init()
    engine.say(summary)
    engine.runAndWait()
    st.success("Lecture terminée.")
