import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
import pandas as pd
from strategy.predictability_index import compute_hourly_predictability, assign_session

st.title("📈 Prédictibilité horaire – UB")

# Chargement des données
df = pd.read_csv("data/donnees_UB.csv")

# Préparation des colonnes nécessaires
df["timestamp"] = pd.to_datetime(df["Start"])
df["outcome"] = (df["Close"] > df["Open"]).astype(int)  # outcome = 1 si le signal est gagnant
df["signal"] = 1  # signal constant pour test initial

# Calcul des scores horaires
scores = compute_hourly_predictability(df)

# Affichage Streamlit
st.subheader("🕒 Prédictibilité par heure (UTC)")
for hour, score in scores.items():
    st.write(f"{hour:02d}h : {score*100:.1f}% de réussite")

# Calcul et affichage par session
df["session"] = df["timestamp"].apply(assign_session)
session_scores = df.groupby("session")["outcome"].mean().round(3)

st.subheader("📊 Prédictibilité par session")
for session, score in session_scores.items():
    st.write(f"{session} : {score*100:.1f}% de réussite")

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

st.title("📈 Prédictibilité horaire – UB")

# Chargement des données
df = pd.read_csv("data/donnees_UB.csv")
df["timestamp"] = pd.to_datetime(df["Start"])
df["outcome"] = (df["Close"] > df["Open"]).astype(int)
df["signal"] = 1
df["session"] = df["timestamp"].apply(assign_session)

# Sélecteur de session
session_choice = st.selectbox("🗂️ Choisissez une session :", ["Toutes", "Asia", "London", "New York", "Off"])

# Filtrage des données
if session_choice != "Toutes":
    df = df[df["session"] == session_choice]

# Calcul des scores horaires
scores = compute_hourly_predictability(df)

        # Affichage des scores horaires
st.subheader(f"🕒 Prédictibilité par heure (UTC) – Session : {session_choice}")
for hour, score in scores.items():
    st.write(f"{hour:02d}h : {score*100:.1f}% de réussite")

# Affichage conditionnel de la distribution horaire
if st.checkbox("🧪 Afficher la distribution horaire"):
    hour_counts = df["timestamp"].dt.hour.value_counts().sort_index()
    st.subheader("Distribution des heures dans les données")
    for hour, count in hour_counts.items():
        st.write(f"{hour:02d}h : {count} entrées")

# Calcul et affichage par session (si toutes sessions)
if session_choice == "Toutes":
    session_scores = df.groupby("session")["outcome"].mean().round(3)
    st.subheader("📊 Prédictibilité par session")
    for session, score in session_scores.items():
        st.write(f"{session} : {score*100:.1f}% de réussite")

st.subheader("🧪 Distribution des heures dans les données")
hour_counts = df["timestamp"].dt.hour.value_counts().sort_index()
for hour, count in hour_counts.items():
    st.write(f"{hour:02d}h : {count} entrées")

