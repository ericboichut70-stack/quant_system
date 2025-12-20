# 🧭 Visualisation des scripts utilitaires
import streamlit as st
import yaml

st.set_page_config(page_title="🧭 Index des scripts", layout="wide")
st.title("🧭 Scripts utilitaires — Private Assistant")

with open("config/bot_registry_scripts.yaml", "r") as f:
    scripts = yaml.safe_load(f)

for name, meta in scripts.items():
    with st.expander(f"📄 {name}", expanded=False):
        st.markdown(f"- **Rôle** : {meta['rôle']}")
        st.markdown(f"- **Génère** : `{meta['génère']}`")
        st.markdown(f"- **Source** : `{meta['source']}`")
