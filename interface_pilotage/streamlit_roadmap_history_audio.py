# 🔊 Rapport vocal de l’historique des roadmaps
import streamlit as st
import yaml
import pyttsx3

st.set_page_config(page_title="🔊 Historique roadmap", layout="centered")
st.title("🔊 Synthèse vocale — Historique des feuilles de route")

with open("config/bot_roadmap_history.yaml", "r") as f:
    history = yaml.safe_load(f)

summary = "🗂️ Historique des roadmaps :\n"
for entry in history:
    summary += f"Version {entry['version']} — {entry['date']}\n"
    for obj in entry["objectifs"]:
        summary += f"- Objectif : {obj}\n"
    for step in entry["étapes"]:
        if "[x]" in step:
            summary += f"- Réalisé : {step.replace('[x]', '').strip()}\n"
    summary += "\n"

st.text_area("📝 Rapport vocal historique :", summary, height=300)

if st.button("🔊 Lire à voix haute"):
    engine = pyttsx3.init()
    engine.say(summary)
    engine.runAndWait()
    st.success("Lecture terminée.")
