# 📚 Visualisation des engagements, signatures et attestations
import streamlit as st
import yaml
import os

st.set_page_config(page_title="📚 Contrats Projet", layout="wide")
st.title("📚 Engagements, signatures et attestations — Private Assistant")

files = {
    "Engagements": "config/bot_roadmap_commitments.yaml",
    "Signatures": "config/bot_roadmap_signatures.yaml",
    "Attestations": "config/bot_roadmap_attestations.md"
}

for label, path in files.items():
    st.subheader(f"📄 {label}")
    if not os.path.exists(path):
        st.warning(f"⚠️ Fichier introuvable : {path}")
        continue

    if path.endswith(".yaml"):
        with open(path, "r") as f:
            data = yaml.safe_load(f)
        for key, value in data.items():
            st.markdown(f"**🔹 {key}** : `{value}`")
    else:
        with open(path, "r") as f:
            content = f.read()
        st.text_area(f"📝 Contenu de {label}", content, height=300)

# 📚 Résumé vocal
st.subheader("🔊 Synthèse vocale du manifeste")

audio_path = "exports/audio/onboarding_manifest_summary.wav"
if os.path.exists(audio_path):
    st.audio(audio_path, format="audio/wav")
    st.success("✅ Résumé vocal du manifeste prêt à l’écoute.")
else:
    st.warning("⚠️ Fichier audio non trouvé.")
