# 📁 Visualisation des dossiers et fichiers avec rôle et usage
import streamlit as st
import os
import yaml

st.set_page_config(page_title="📁 Structure Projet", layout="wide")
st.title("📁 Visualisation des dossiers et fichiers — Private Assistant")

def render_folder(path, level=0):
    indent = " " * level
    for item in sorted(os.listdir(path)):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            st.markdown(f"{indent}📁 **{item}**")
            render_folder(full_path, level + 1)
        else:
            st.markdown(f"{indent}📄 {item}")

st.subheader("🗂️ Arborescence du projet")
render_folder(".")

st.subheader("📘 Rôles et usages des fichiers audio")
audio_index_path = "config/bot_registry_audio.yaml"
if os.path.exists(audio_index_path):
    with open(audio_index_path, "r") as f:
        audio_index = yaml.safe_load(f)
    for filename, meta in audio_index.items():
        st.markdown(f"**🎙️ {filename}**")
        st.markdown(f"- Rôle : {meta['rôle']}")
        st.markdown(f"- Usage : {meta['usage']}")
else:
    st.warning("⚠️ Fichier `bot_registry_audio.yaml` non trouvé.")
