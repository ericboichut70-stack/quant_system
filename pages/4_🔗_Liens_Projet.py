# ✅ Visualiseur des liens pour navigation directe.
import streamlit as st
import yaml

st.set_page_config(page_title="🔗 Liens du projet", layout="wide")
st.title("🔗 Visualiseur des liens — Private Assistant")

with open("config/bot_registry_links.yaml", "r") as f:
    links = yaml.safe_load(f)

for key, meta in links.items():
    with st.expander(meta["label"], expanded=False):
        st.markdown(f"**📁 Chemin** : `{meta['chemin']}`")
        if "export_md" in meta:
            st.markdown(f"**📝 Export .md** : `{meta['export_md']}`")
        if "capture" in meta:
            st.markdown(f"**🖼️ Capture** : `{meta['capture']}`")
