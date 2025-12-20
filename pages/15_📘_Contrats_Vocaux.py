# 📘 Ecoute et validation des blocs contractuels
import streamlit as st
import yaml
import os

st.set_page_config(page_title="📘 Contrats Vocaux", layout="wide")
st.title("📘 Validation des blocs contractuels — Private Assistant")

# 🔊 Synthèses vocales
st.subheader("🔊 Synthèses vocales contractuelles")
audio_files = [
    "onboarding_manifest_summary.wav",
    "onboarding_manifest_summary.mp3"
]
for audio in audio_files:
    path = os.path.join("exports/audio", audio)
    if os.path.exists(path):
        st.markdown(f"**🎧 {audio}**")
        st.audio(path, format="audio/wav" if audio.endswith(".wav") else "audio/mp3")
    else:
        st.warning(f"⚠️ Fichier audio non trouvé : {audio}")

# 📘 Fichiers contractuels
st.subheader("📘 Blocs contractuels")
files = {
    "Engagements": "config/bot_roadmap_commitments.yaml",
    "Signatures": "config/bot_roadmap_signatures.yaml",
    "Attestations": "config/bot_roadmap_attestations.md"
}
for label, path in files.items():
    st.markdown(f"### 📄 {label}")
    if not os.path.exists(path):
        st.warning(f"⚠️ Fichier introuvable : {path}")
        continue
    if path.endswith(".yaml"):
        with open(path, "r") as f:
            data = yaml.safe_load(f)
        for key, value in data.items():
            st.markdown(f"- **{key}** : `{value}`")
    else:
        with open(path, "r") as f:
            content = f.read()
        st.text_area(f"📝 Contenu de {label}", content, height=300)

# 🔊 Intégrer la synthèse vocale finale dans la page Contrats Vocaux
st.subheader("✅ Synthèse vocale de validation finale")

final_audio = "exports/audio/onboarding_validation_summary.wav"
if os.path.exists(final_audio):
    st.audio(final_audio, format="audio/wav")
    st.success("✅ Synthèse finale prête à l’écoute.")
else:
    st.warning("⚠️ Fichier audio non trouvé.")

# 📘 Ajout de bot_registry_index_contrats.yaml
st.subheader("📘 Index des contrats vocaux")

contrats_index_path = "config/bot_registry_index_contrats.yaml"
if os.path.exists(contrats_index_path):
    with open(contrats_index_path, "r") as f:
        contrats_index_content = f.read()
    st.text_area("📘 Contenu du fichier index_contrats", contrats_index_content, height=300)
else:
    st.warning("⚠️ Fichier index des contrats introuvable.")
