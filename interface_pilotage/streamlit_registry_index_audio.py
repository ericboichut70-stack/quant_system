# 🔊 Rapport vocal des artefacts par version
import streamlit as st
import yaml
import pyttsx3

st.set_page_config(page_title="🔊 Artefacts roadmap", layout="centered")
st.title("🔊 Synthèse vocale — Artefacts par version")

with open("config/bot_roadmap_registry.yaml", "r") as f:
    registry = yaml.safe_load(f)

summary = "🗂️ Artefacts roadmap :\n"
for version, data in registry.items():
    summary += f"Version {version} :\n"
    for key, value in data.items():
        if isinstance(value, list):
            summary += f"- {key} : {', '.join(value)}\n"
        else:
            summary += f"- {key} : {value}\n"
    summary += "\n"

st.text_area("📝 Synthèse vocale du registre :", summary, height=300)

if st.button("🔊 Lire à voix haute"):
    engine = pyttsx3.init()
    engine.say(summary)
    engine.runAndWait()
    st.success("Lecture terminée.")
