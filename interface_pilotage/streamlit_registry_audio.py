# 🔊 Rapport vocal du registre roadmap
import streamlit as st
import yaml
import pyttsx3

st.set_page_config(page_title="🔊 Registre roadmap", layout="centered")
st.title("🔊 Synthèse vocale — Registre roadmap")

with open("config/bot_roadmap_registry.yaml", "r") as f:
    registry = yaml.safe_load(f)

summary = "📚 Registre roadmap :\n"
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
