# 🔊 Résumé vocal des évolutions entre versions
import streamlit as st
import yaml
import pyttsx3

st.set_page_config(page_title="🔊 Évolutions du bot", layout="centered")
st.title("🔊 Synthèse vocale — évolutions entre versions")

with open("config/bot_changelog.yaml", "r") as f:
    changelog = yaml.safe_load(f)

summary = "🧾 Évolutions du bot Private Assistant :\n"
for entry in changelog:
    summary += f"Version {entry['version']} — {entry['date']} :\n"
    for commit in entry["commits"]:
        summary += f"- {commit}\n"

st.text_area("📝 Résumé vocal :", summary, height=300)

if st.button("🔊 Lire à voix haute"):
    engine = pyttsx3.init()
    engine.say(summary)
    engine.runAndWait()
    st.success("Lecture terminée.")
