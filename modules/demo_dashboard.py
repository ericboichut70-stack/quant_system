from modules.public_demo import public_demo_interface
# 📊 Appel interface publique de démonstration
st.subheader("🌐 Démonstration publique")
demo_signal = {"ScenarioType": "breakout", "ConfidenceScore": 7}
demo_memory_dict = {"breakout": 6, "range": -2}

demo_feedback = public_demo_interface(demo_signal, demo_memory_dict)
st.markdown(demo_feedback)