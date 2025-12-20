# 🌐 Liens, fichiers et audio publics
import streamlit as st
import os
import yaml

st.set_page_config(page_title="🌐 Partage Externe", layout="wide")
st.title("🌐 Diffusion publique — Private Assistant")

index_path = "config/bot_registry_public.yaml"
if not os.path.exists(index_path):
    st.warning("⚠️ Fichier `bot_registry_public.yaml` introuvable.")
else:
    with open(index_path, "r") as f:
        public_index = yaml.safe_load(f)

    for section, files in public_index.items():
        st.subheader(f"📁 {section}")
        for file in files:
            path = os.path.join("exports", "audio" if "mp3" in file or "wav" in file else "", file)
            if os.path.exists(path):
                if file.endswith(".mp3") or file.endswith(".wav"):
                    st.markdown(f"**🎧 {file}**")
                    st.audio(path, format="audio/mp3" if file.endswith(".mp3") else "audio/wav")
                else:
                    st.markdown(f"- 📄 `{file}`")
            else:
                st.warning(f"⚠️ Fichier manquant : {file}")

# 📘 Ajout de onboarding_export_summary.mp3
# Permet d’exposer la synthèse publique d’export consolidé dans la diffusion externe.
st.subheader("🔊 Synthèse vocale d’export public")

export_audio = "exports/audio/onboarding_export_summary.mp3"
if os.path.exists(export_audio):
    st.audio(export_audio, format="audio/mp3")
    st.success("✅ Synthèse publique d’export prête à l’écoute.")
else:
    st.warning("⚠️ Fichier audio non trouvé.")

# 🌐 Ajout de bot_registry_public.yaml
st.subheader("📘 Registre des fichiers publics")

public_path = "config/bot_registry_public.yaml"
if os.path.exists(public_path):
    with open(public_path, "r") as f:
        public_content = f.read()
    st.text_area("📘 Contenu du registre public", public_content, height=300)
else:
    st.warning("⚠️ Fichier de registre public introuvable.")

# 🌐 Ajout de bot_registry_attestation_publique.md
st.subheader("📜 Attestation publique (markdown)")

attestation_publique_path = "config/bot_registry_attestation_publique.md"
if os.path.exists(attestation_publique_path):
    with open(attestation_publique_path, "r") as f:
        attestation_publique_content = f.read()
    st.text_area("📘 Contenu de l’attestation publique", attestation_publique_content, height=300)
else:
    st.warning("⚠️ Fichier d’attestation publique introuvable.")

# 🌐 Ajout de bot_registry_index_diffusion.yaml
st.subheader("📘 Index de diffusion publique")

diffusion_index_path = "config/bot_registry_index_diffusion.yaml"
if os.path.exists(diffusion_index_path):
    with open(diffusion_index_path, "r") as f:
        diffusion_index_content = f.read()
    st.text_area("🌐 Contenu du fichier index_diffusion", diffusion_index_content, height=300)
else:
    st.warning("⚠️ Fichier index de diffusion introuvable.")
