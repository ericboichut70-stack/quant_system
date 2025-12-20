# 🔊 Résumé vocal des liens et raccourcis pour onboarding rapide
import streamlit as st
import yaml
import pyttsx3

st.set_page_config(page_title="🔊 Liens du projet", layout="centered")
st.title("🔊 Synthèse vocale — Liens et raccourcis")

with open("config/bot_registry_links.yaml", "r") as f:
    links = yaml.safe_load(f)

summary = "🔗 Liens et raccourcis du projet :\n"
for key, meta in links.items():
    summary += f"{meta['label']} : {meta['chemin']}\n"
    if "export_md" in meta:
        summary += f"Export markdown : {meta['export_md']}\n"
    if "capture" in meta:
        summary += f"Capture : {meta['capture']}\n"
    summary += "\n"

st.text_area("📝 Synthèse vocale des liens :", summary, height=300)

if st.button("🔊 Lire à voix haute"):
    engine = pyttsx3.init()
    engine.say(summary)
    engine.runAndWait()
    st.success("Lecture terminée.")
