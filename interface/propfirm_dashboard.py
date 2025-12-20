import streamlit as st
from strategy.propfirm_rules import enforce_rules

strategy_profile = {
    "max_drawdown": 9.5,
    "daily_loss": 5.5,
    "uses_scalping": True
}

propfirms = ["FTMO", "MyForexFunds", "The5ers"]

st.title("🧠 Propfirm Compatibility Checker")

for firm in propfirms:
    try:
        enforce_rules(firm, strategy_profile)
        st.success(f"✅ {firm} compatible")
    except Exception as e:
        st.error(str(e))

import streamlit as st
import pandas as pd
from strategy.predictability_index import compute_hourly_predictability

st.title("📈 Prédictibilité horaire – UB")

df = pd.read_csv("data/donnees_UB.csv", parse_dates=["timestamp"])
scores = compute_hourly_predictability(df)

st.subheader("Indice de prédictibilité par heure (UTC)")
for hour, score in scores.items():
    st.write(f"{hour:02d}h : {score*100:.1f}% de réussite")
