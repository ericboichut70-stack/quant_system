# 🧠 Intentions, validations, signatures
import streamlit as st
import yaml
import os

st.set_page_config(page_title="🧠 Mémoire Projet", layout="wide")
st.title("🧠 Mémoire du projet — Private Assistant")

st.markdown("Explore les intentions, validations, signatures et attestations du projet.")

files = {
    "Intentions": "config/bot_roadmap_commitments.yaml",
    "Signatures": "config/bot_roadmap_signatures.yaml",
    "Attestations": "config/bot_roadmap_attestations.md",
    "Validation": "config/bot_registry_validation.yaml",
    "Soumission": "config/bot_registry_submission.yaml",
    "Attestation": "config/bot_registry_attestation.yaml"
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
            if isinstance(value, list):
                st.markdown(f"**🔹 {key}**")
                for item in value:
                    st.markdown(f"- {item}")
            else:
                st.markdown(f"- **{key}** : `{value}`")
    else:
        with open(path, "r") as f:
            content = f.read()
        st.text_area(f"📝 Contenu de {label}", content, height=300)

# Ajout synthèse vocale de mémoire
st.subheader("🔊 Synthèse vocale de mémoire")

memory_audio = "exports/audio/onboarding_memory_summary.wav"
if os.path.exists(memory_audio):
    st.audio(memory_audio, format="audio/wav")
    st.success("✅ Synthèse de mémoire prête à l’écoute.")
else:
    st.warning("⚠️ Fichier audio non trouvé.")

# 🧠 Ajout de bot_registry_validation_cross.yaml
st.subheader("📘 Validation croisée")

cross_path = "config/bot_registry_validation_cross.yaml"
if os.path.exists(cross_path):
    with open(cross_path, "r") as f:
        cross_content = f.read()
    st.text_area("🧠 Validation croisée YAML", cross_content, height=300)
else:
    st.warning("⚠️ Fichier de validation croisée introuvable.")

# 📜 Ajout de bot_registry_synthese_finale.yaml
st.subheader("🧠 Synthèses vocales finales")

synthese_path = "config/bot_registry_synthese_finale.yaml"
if os.path.exists(synthese_path):
    with open(synthese_path, "r") as f:
        synthese_content = f.read()
    st.text_area("📘 Index des synthèses finales", synthese_content, height=300)
else:
    st.warning("⚠️ Fichier synthèse finale introuvable.")

# 🧠 Ajout de bot_registry_index_vocal.yaml
st.subheader("📘 Index des synthèses vocales")

vocal_index_path = "config/bot_registry_index_vocal.yaml"
if os.path.exists(vocal_index_path):
    with open(vocal_index_path, "r") as f:
        vocal_index_content = f.read()
    st.text_area("🔊 Index YAML des synthèses MP3", vocal_index_content, height=300)
else:
    st.warning("⚠️ Fichier d’index vocal introuvable.")

# 🧠 Ajout de bot_registry_onboarding_vocal.yaml
st.subheader("📘 Synthèses d’onboarding")

onboarding_vocal_path = "config/bot_registry_onboarding_vocal.yaml"
if os.path.exists(onboarding_vocal_path):
    with open(onboarding_vocal_path, "r") as f:
        onboarding_vocal_content = f.read()
    st.text_area("🔊 Index YAML des synthèses d’onboarding", onboarding_vocal_content, height=300)
else:
    st.warning("⚠️ Fichier d’onboarding vocal introuvable.")

# 🧠 Ajout de bot_registry_index_synthese.yaml
st.subheader("🧠 Index synthétique final")

synthese_finale_path = "config/bot_registry_index_synthese.yaml"
if os.path.exists(synthese_finale_path):
    with open(synthese_finale_path, "r") as f:
        synthese_finale_content = f.read()
    st.text_area("📘 Contenu du fichier synthèse finale", synthese_finale_content, height=300)
else:
    st.warning("⚠️ Fichier synthèse finale introuvable.")

# 🧠 Ajout de bot_registry_index_complet.yaml
st.subheader("🧠 Index complet vocal + manifeste")

index_complet_path = "config/bot_registry_index_complet.yaml"
if os.path.exists(index_complet_path):
    with open(index_complet_path, "r") as f:
        index_complet_content = f.read()
    st.text_area("📘 Contenu du fichier index complet", index_complet_content, height=300)
else:
    st.warning("⚠️ Fichier index complet introuvable.")

# 🧠 Ajout de bot_registry_validation_cross.yaml
st.subheader("🧠 Index de validation croisée")

validation_cross_path = "config/bot_registry_validation_cross.yaml"
if os.path.exists(validation_cross_path):
    with open(validation_cross_path, "r") as f:
        validation_cross_content = f.read()
    st.text_area("📘 Contenu du fichier validation_cross", validation_cross_content, height=300)
else:
    st.warning("⚠️ Fichier validation croisée introuvable.")

# 🧠 Ajout de bot_registry_index_memoire.yaml
st.subheader("📘 Index mémoire finale")

memoire_index_path = "config/bot_registry_index_memoire.yaml"
if os.path.exists(memoire_index_path):
    with open(memoire_index_path, "r") as f:
        memoire_index_content = f.read()
    st.text_area("🧠 Contenu du fichier index mémoire", memoire_index_content, height=300)
else:
    st.warning("⚠️ Fichier index mémoire introuvable.")

# 🧠 Ajout de bot_registry_index_synthese.yaml
st.subheader("📘 Index de synthèse finale")

synthese_index_path = "config/bot_registry_index_synthese.yaml"
if os.path.exists(synthese_index_path):
    with open(synthese_index_path, "r") as f:
        synthese_index_content = f.read()
    st.text_area("🧠 Contenu du fichier index_synthese", synthese_index_content, height=300)
else:
    st.warning("⚠️ Fichier index de synthèse introuvable.")

# 🧠 Ajout de bot_registry_cloture_finale.yaml
st.subheader("📘 Clôture consolidée")

cloture_finale_path = "config/bot_registry_cloture_finale.yaml"
if os.path.exists(cloture_finale_path):
    with open(cloture_finale_path, "r") as f:
        cloture_finale_content = f.read()
    st.text_area("🔐 Contenu du fichier cloture_finale", cloture_finale_content, height=300)
else:
    st.warning("⚠️ Fichier de clôture consolidée introuvable.")

# 🔊 onboarding_cloture_finale_summary.txt
Clôture finale du système Private Assistant.

Toutes les séries d’intégration ont été menées à terme, sans exception.  
Chaque fichier index a été activé, structuré, intégré dans le manifeste, l’archive, et les pages associées.  
Les blocs de synthèse, de mémoire, de validation, de certification, d’attestation, d’export et de diffusion sont tous verrouillés.

Le projet est désormais consolidé, traçable, et prêt pour l’audit collaboratif.  
Chaque artefact est documenté, chaque usage est référencé, chaque page est activée.

Ce système est vivant, navigable, et prêt pour l’onboarding futur.  
Clôture validée. Archivage final enclenché.  
Private Assistant est certifié, autonome, et historiquement complet.
