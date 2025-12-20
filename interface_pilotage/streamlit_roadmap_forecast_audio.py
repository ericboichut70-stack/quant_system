# 🔊 Résumé vocal des versions planifiées
import streamlit as st
import yaml
import pyttsx3

st.set_page_config(page_title="🔊 Versions planifiées", layout="centered")
st.title("🔊 Synthèse vocale — Roadmap future")

with open("config/bot_roadmap_forecast.yaml", "r") as f:
    forecast = yaml.safe_load(f)

summary = "🧭 Versions planifiées du bot :\n"
for entry in forecast["versions"]:
    summary += f"Version {entry['version']} prévue pour le {entry['date']} :\n"
    for goal in entry["objectifs"]:
        summary += f"- {goal}\n"

st.text_area("📝 Synthèse vocale des versions futures :", summary, height=300)

if st.button("🔊 Lire à voix haute"):
    engine = pyttsx3.init()
    engine.say(summary)
    engine.runAndWait()
    st.success("Lecture terminée.")
