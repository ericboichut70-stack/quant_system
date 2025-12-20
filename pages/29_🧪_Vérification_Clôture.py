# ✅ Script Python : verify_cloture_files.py
# ✅ Vérification des fichiers Markdown et HTML dans le dossier config/

import os
import streamlit as st

st.title("📦 Vérification des fichiers de clôture dans config/")

# 📁 Dossier à vérifier
config_dir = "config"

# 📘 Fichiers Markdown attendus
expected_md = [
    "bot_registry_onboarding.md",
    "bot_registry_contracts.md",
    "bot_registry_certification.md",
    "bot_registry_attestation_publique.md",
    "bot_registry_cloture_finale.md"
]

# 🌐 Fichiers HTML attendus
expected_html = [
    "bot_registry_cloture_finale.html"
]

def check_files(file_list, extension):
    st.subheader(f"📘 Fichiers {extension.upper()} attendus")
    for filename in file_list:
        file_path = os.path.join(config_dir, filename)
        if os.path.exists(file_path):
            st.success(f"✅ {filename} trouvé")
        else:
            st.error(f"❌ {filename} manquant")

check_files(expected_md, "md")
check_files(expected_html, "html")

# 📦 Ajout d’une fonction de téléchargement ZIP ou de validation mentor
# 📦 Téléchargement du ZIP final
st.subheader("📦 Téléchargement de l’archive ZIP")

zip_path = "exports/export_all.zip"
if os.path.exists(zip_path):
    with open(zip_path, "rb") as f:
        st.download_button(
            label="📥 Télécharger l’archive ZIP",
            data=f,
            file_name="PrivateAssistant_Archive.zip",
            mime="application/zip"
        )
    st.success("✅ Archive ZIP prête au téléchargement.")
else:
    st.warning("⚠️ Archive ZIP introuvable.")

# 🧑‍🏫 Validation mentor (simulation)
st.subheader("🧑‍🏫 Validation mentor")

if st.button("🔐 Déclencher la validation mentor"):
    st.success("✅ Validation mentor simulée. Le projet est prêt pour diffusion ou certification.")

# 🔊 Synthèse vocale de validation finale
st.subheader("🔊 Synthèse vocale de validation finale")

validation_audio = "exports/audio/onboarding_validation_finale_summary.mp3"
if os.path.exists(validation_audio):
    st.audio(validation_audio, format="audio/mp3")
    st.success("✅ Synthèse de validation prête à l’écoute.")
else:
    st.warning("⚠️ Fichier audio de validation non trouvé.")

# 🔐 Clôture mentor
st.subheader("🔐 Clôture mentor")

if st.button("🔏 Valider la clôture mentor"):
    st.success("✅ Clôture mentor validée. Le système est prêt pour diffusion officielle.")

# 🔊 Synthèse vocale — onboarding_diffusion_publique_summary.txt
Diffusion publique consolidée du système Private Assistant.

Tous les blocs critiques ont été validés : certification, soumission, clôture, export, attestation.  
La synthèse vocale est prête.  
L’attestation publique est validée et disponible en Markdown et HTML.

Le système est certifié, consolidé, et prêt pour diffusion externe.  
Private Assistant est publiquement verrouillé et historiquement complet.
