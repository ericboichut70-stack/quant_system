# 🔊 Rapport vocal de conformité certifiée
with open("config/module_registry.yaml", "r") as f:
    registry = yaml.safe_load(f)

certified = [name for name, data in registry.items() if data["status"] == "verrouillé" and data["score"] >= 80]
summary = f"📜 Le bot est certifié avec {len(certified)} module(s) validé(s).\n"
for name in certified:
    summary += f"{name} — score {registry[name]['score']}\n"

st.text_area("📝 Rapport vocal de conformité :", summary, height=200)

if st.button("🔊 Lire à voix haute"):
    engine = pyttsx3.init()
    engine.say(summary)
    engine.runAndWait()
    st.success("Lecture terminée.")
