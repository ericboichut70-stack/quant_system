# 🔊 Rapport vocal des actions comptables
import streamlit as st
import yaml
import pyttsx3

st.set_page_config(page_title="🔊 Registre comptable", layout="centered")
st.title("🔊 Synthèse vocale — Actions de livraison")

with open("config/bot_registry_ledger.yaml", "r") as f:
    ledger = yaml.safe_load(f)

summary = "📒 Registre comptable des livraisons :\n"
for entry in ledger:
    summary += f"{entry['date']} — Version {entry['version']}, action : {entry['action']}, validé par {entry['validé_par']}.\n"

st.text_area("📝 Synthèse vocale du ledger :", summary, height=300)

if st.button("🔊 Lire à voix haute"):
    engine = pyttsx3.init()
    engine.say(summary)
    engine.runAndWait()
    st.success("Lecture terminée.")
