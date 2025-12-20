# 🧠 Centre d’onboarding vocal et documentaire
import streamlit as st
import os
import yaml

st.set_page_config(page_title="🧠 Synthèse Onboarding", layout="wide")
st.title("🧠 Centre d’onboarding vocal et documentaire — Private Assistant")

# 📘 Fichiers markdown
st.subheader("📘 Documentation externe")
md_files = [
    "bot_registry_links_summary.md",
    "bot_registry_audio.md"
]
for md in md_files:
    path = os.path.join("exports", md)
    if os.path.exists(path):
        st.markdown(f"- 📄 `{md}`")
    else:
        st.warning(f"⚠️ Fichier manquant : {md}")

# 🔉 Fichiers audio
st.subheader("🔉 Synthèses vocales")
audio_files = [
    "onboarding_links.wav",
    "onboarding_links.mp3",
    "audio_roles_summary.wav"
]
for audio in audio_files:
    path = os.path.join("exports/audio", audio)
    if os.path.exists(path):
        st.markdown(f"**🎧 {audio}**")
        st.audio(path, format="audio/wav" if audio.endswith(".wav") else "audio/mp3")
    else:
        st.warning(f"⚠️ Fichier audio non trouvé : {audio}")

# ▶️ Bouton “Tout écouter”
st.subheader("▶️ Lecture enchaînée")
if st.button("🔁 Écouter toutes les synthèses vocales"):
    for audio in audio_files:
        path = os.path.join("exports/audio", audio)
        if os.path.exists(path):
            st.audio(path, format="audio/wav" if audio.endswith(".wav") else "audio/mp3")

st.markdown("---")
st.info("Tous les fichiers sont intégrés dans le manifeste et l’archive pour traçabilité complète.")

# 📂 Bouton “Ouvrir tous les exports” dans la page Synthèse Onboarding
st.subheader("📂 Accès global aux exports")

if st.button("📘 Ouvrir tous les exports"):
    st.markdown("➡️ Navigue dans le menu latéral à gauche : **🧠 Synthèse Onboarding**")
    st.info("Tous les fichiers `.md`, `.wav`, `.mp3` sont listés ci-dessous pour consultation directe.")

# 🧠 Résumé final
st.subheader("🔊 Synthèse finale du projet")

final_audio = "exports/audio/onboarding_final_summary.wav"
if os.path.exists(final_audio):
    st.audio(final_audio, format="audio/wav")
    st.success("✅ Résumé vocal final prêt à l’écoute.")
else:
    st.warning("⚠️ Fichier `onboarding_final_summary.wav` non trouvé.")

# 🧠 Ajout de bot_registry_index_onboarding.yaml
st.subheader("📘 Index d’onboarding final")

onboarding_index_path = "config/bot_registry_index_onboarding.yaml"
if os.path.exists(onboarding_index_path):
    with open(onboarding_index_path, "r") as f:
        onboarding_index_content = f.read()
    st.text_area("🧠 Contenu du fichier index_onboarding", onboarding_index_content, height=300)
else:
    st.warning("⚠️ Fichier index d’onboarding introuvable.")
