# 🗂️ Visualiseur Streamlit des usages vocaux par rôle
import streamlit as st
import yaml

st.set_page_config(page_title="🗂️ Usages vocaux", layout="wide")
st.title("🗂️ Visualisation des usages vocaux — Private Assistant")

with open("config/bot_registry_audio.yaml", "r") as f:
    audio_index = yaml.safe_load(f)

roles = {}
for filename, meta in audio_index.items():
    rôle = meta["rôle"]
    if rôle not in roles:
        roles[rôle] = []
    roles[rôle].append((filename, meta))

for rôle, items in roles.items():
    with st.expander(f"🎙️ {rôle}", expanded=False):
        for filename, meta in items:
            st.markdown(f"**📄 {filename}**")
            st.markdown(f"- Format : `{meta['format']}`")
            st.markdown(f"- Source : `{meta['source']}`")
            st.markdown(f"- Usage : {meta['usage']}")
            st.audio(f"exports/audio/{filename}", format=f"audio/{meta['format']}")
