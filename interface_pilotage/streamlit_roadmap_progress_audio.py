# 🔊 Rapport vocal de progression roadmap
import streamlit as st
import yaml
import pyttsx3

st.set_page_config(page_title="🔊 Progression roadmap", layout="centered")
st.title("🔊 Synthèse vocale — Progression de la roadmap")

with open("config/bot_roadmap.yaml", "r") as f:
    roadmap = yaml.safe_load(f)

summary = f"Feuille de route vers la version {roadmap['next_version']}.\n"
summary += f"Date prévue : {roadmap['planned_date']}.\n"
summary += "Étapes réalisées :\n"

for step in roadmap["étapes"]:
    if "[x]" in step:
        summary += f"- {step.replace('[x]', '').strip()}\n"

summary += "Étapes restantes :\n"
for step in roadmap["étapes"]:
    if "[ ]" in step:
        summary += f"- {step.replace('[ ]', '').strip()}\n"

st.text_area("📝 Rapport vocal de progression :", summary, height=300)

if st.button("🔊 Lire à voix haute"):
    engine = pyttsx3.init()
    engine.say(summary)
    engine.runAndWait()
    st.success("Lecture terminée.")
