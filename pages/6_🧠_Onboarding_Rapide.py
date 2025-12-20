# 🧠 Accès essentiels
import streamlit as st
import yaml

st.set_page_config(page_title="🧠 Onboarding rapide", layout="wide")
st.title("🧠 Accès rapide — Private Assistant")

st.markdown("Bienvenue dans le centre d’activation rapide du projet. Voici les accès essentiels :")

with open("config/bot_registry_links.yaml", "r") as f:
    links = yaml.safe_load(f)

for key, meta in links.items():
    with st.expander(meta["label"], expanded=False):
        st.markdown(f"**📁 Chemin** : `{meta['chemin']}`")
        if "export_md" in meta:
            st.markdown(f"**📝 Export .md** : `{meta['export_md']}`")
        if "capture" in meta:
            st.markdown(f"**🖼️ Capture** : `{meta['capture']}`")

st.markdown("---")
st.markdown("🔊 Pour une synthèse vocale, utilise le bouton dans le dashboard principal.")
