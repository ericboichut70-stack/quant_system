# 🔊 Rapport vocal des artefacts archivés
import streamlit as st
import yaml
import pyttsx3

st.set_page_config(page_title="🔊 Archive roadmap", layout="centered")
st.title("🔊 Synthèse vocale — Artefacts archivés")

with open("config/bot_registry_archive.yaml", "r") as f:
    archive = yaml.safe_load(f)

summary = "📦 Artefacts archivés :\n"
for entry in archive:
    summary += f"Version {entry['version']} — {entry['date']}\n"
    for art in entry["artefacts"]:
        summary += f"- {art}\n"
    summary += "\n"

st.text_area("📝 Synthèse vocale de l’archive :", summary, height=300)

if st.button("🔊 Lire à voix haute"):
    engine = pyttsx3.init()
    engine.say(summary)
    engine.runAndWait()
    st.success("Lecture terminée.")
