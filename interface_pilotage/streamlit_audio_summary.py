# 🔊 Résumé vocal du rapport via interface audio
import streamlit as st
import yaml
import pyttsx3

st.set_page_config(page_title="🎧 Résumé vocal", layout="centered")
st.title("🎧 Résumé vocal — Rapport final")

with open("config/bot_metrics.yaml", "r") as f:
    metrics = yaml.safe_load(f)

summary = f"""
Le bot Private Assistant contient {metrics['total_modules']} modules.
{metrics['verrouillés']} sont verrouillés, avec un score moyen de {metrics['score_moyen_verrouillés']}.
{metrics['en_test']} sont en cours de test, avec un score moyen de {metrics['score_moyen_testés']}.
La progression globale est de {metrics['progression_globale'] * 100:.1f} pourcent.
"""

st.text_area("📝 Résumé généré :", summary, height=150)

if st.button("🔊 Lire à voix haute"):
    engine = pyttsx3.init()
    engine.say(summary)
    engine.runAndWait()
    st.success("Lecture terminée.")
