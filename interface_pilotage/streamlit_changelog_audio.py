# 🔊 Rapport vocal des ajouts et corrections par version
import streamlit as st
import yaml
import pyttsx3

st.set_page_config(page_title="🔊 Changelog modulaire", layout="centered")
st.title("🔊 Synthèse vocale — Changements par version")

with open("config/bot_registry_changelog.yaml", "r") as f:
    changelog = yaml.safe_load(f)

summary = "🧮 Changements par version :\n"
for version, data in changelog.items():
    summary += f"Version {version} :\n"
    for key, items in data.items():
        if items:
            summary += f"{key.capitalize()} : {', '.join(items)}\n"
    summary += "\n"

st.text_area("📝 Synthèse vocale du changelog :", summary, height=300)

if st.button("🔊 Lire à voix haute"):
    engine = pyttsx3.init()
    engine.say(summary)
    engine.runAndWait()
    st.success("Lecture terminée.")
