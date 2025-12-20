# 🔊 Rapport vocal des validations mentor
with open("config/module_registry.yaml", "r") as f:
    registry = yaml.safe_load(f)

summary = "🧑‍🏫 Synthèse des validations mentor :\n"
for name, data in registry.items():
    if "mentor_comment" in data:
        summary += f"{name} : score {data['score']}, commentaire : {data['mentor_comment']}\n"

st.text_area("📝 Résumé vocal mentor :", summary, height=200)

if st.button("🔊 Lire à voix haute"):
    engine = pyttsx3.init()
    engine.say(summary)
    engine.runAndWait()
    st.success("Lecture terminée.")
