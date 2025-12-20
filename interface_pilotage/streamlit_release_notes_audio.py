# 🔊 Rapport vocal des nouveautés par version
import streamlit as st
import yaml
import pyttsx3

st.set_page_config(page_title="🔊 Release notes", layout="centered")
st.title("🔊 Synthèse vocale — Évolutions par version")

notes = {
    "1.0.0": [
        "Verrouillage des modules",
        "Ajout de l’interface mentor",
        "Export vocal des feedbacks",
        "Archivage complet"
    ],
    "0.9.0": [
        "Activation du scoring communautaire",
        "Ajout du module trend_detector",
        "Export CSV des activations"
    ],
    "0.8.0": [
        "Structuration initiale du registre",
        "Déploiement des premiers modules"
    ]
}

summary = "🧾 Évolutions du bot :\n"
for version, changes in notes.items():
    summary += f"Version {version} :\n"
    for change in changes:
        summary += f"- {change}\n"
    summary += "\n"

st.text_area("📝 Synthèse vocale des nouveautés :", summary, height=300)

if st.button("🔊 Lire à voix haute"):
    engine = pyttsx3.init()
    engine.say(summary)
    engine.runAndWait()
    st.success("Lecture terminée.")
