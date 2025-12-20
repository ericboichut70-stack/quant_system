"""
dashboard.py – Interface Streamlit
Affiche les signaux, permet le filtrage par Score IA, visualise les indicateurs et les positions.
"""

import streamlit as st
import pandas as pd
from strategy.signal_filter import filter_signals
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from indicators.ut_pivots import calculate_ut_pivots
from indicators.phoebus_energy import grid_search_energy, plot_energy_histogram
from modules.sentiment_analyzer import analyze_sentiment
from strategy.signal_engine import generate_energy_signals
from strategy.signal_engine import generate_signals
from strategy.signal_engine import generate_energy_signals
from strategy.signal_engine import generate_combined_signals
from modules.optimizer import optimize_parameters
from strategy.signal_engine import summarize_trades
from strategy.signal_engine import filter_signals_by_sentiment
from modules.signal_predictor import train_signal_predictor, predict_signal
from modules.trend_detector import detect_trend
from modules.position_manager import compute_position_parameters

# Dictionnaire de recommandations
parameter_guidance = {
    "RiskReward": "💡 Un ratio > 2.0 est souvent considéré comme optimal pour les setups à forte conviction.",
    "ExpectancyThreshold": "📈 Un seuil d'espérance > 0.2 filtre les actifs avec un potentiel mathématique positif.",
    "Mitigated": "🧠 Les signaux non mitigés sont plus bruts, mais parfois plus risqués.",
    "StructureType": "📚 'bullish' et 'bearish' sont les bases, mais 'range' permet d'explorer les zones de neutralité."
}

# Charger le calendrier des news
news_path = "data/news_calendar/forexfactory_impact.csv"
df_news = pd.read_csv(news_path)
df_news = analyze_sentiment(df_news)

if st.checkbox("📰 Afficher le sentiment des news"):
    st.dataframe(df_news[["timestamp", "title", "impact", "sentiment"]])

# Charger les signaux exportés
df = pd.read_csv("data/signaux_trading.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Afficher le tableau
st.dataframe(df)

# Option : filtrer par score
score_min = st.slider("Score IA minimum", 0, 100, 40)
df_filtered = df[df["ScoreIA"] >= score_min]
st.write("Signaux filtrés :")
st.dataframe(df_filtered)

impact_level = st.selectbox("🎯 Niveau d’impact à filtrer :", ["high", "medium", "low"])
window_minutes = st.slider("⏱️ Fenêtre de détection autour du signal (min)", 5, 60, 30)
turbulence_threshold = st.slider("🌪️ Seuil de turbulence", 0.0, 0.05, 0.02)

news_path = "data/news_calendar/forexfactory_impact.csv"

df_filtered_signals = filter_signals(
    df_filtered,
    news_path=news_path,
    impact_level=impact_level,
    window_minutes=window_minutes,
    turbulence_threshold=turbulence_threshold
)

df_alerts = df_filtered_signals[df_filtered_signals["reason"] != ""]
st.warning(f"{len(df_alerts)} signaux filtrés pour cause de news ou turbulence.")
st.dataframe(df_alerts[["timestamp", "reason", "close"]])

# Calcul des 7 EMA
ema_periods = [19, 38, 57, 76, 95, 114, 133]
for period in ema_periods:
    df_filtered_signals[f"EMA_{period}"] = df_filtered_signals["close"].rolling(window=period).mean()

st.title("BOT IA – Signaux de trading")

import os
os.makedirs("data/logs", exist_ok=True)
df_filtered_signals.to_csv("data/logs/filtered_signals_log.csv", index=False)

import matplotlib.pyplot as plt

st.subheader("📊 Visualisation des signaux filtrés")

fig, ax = plt.subplots(figsize=(10, 5))

# Signaux acceptés
accepted = df_filtered_signals[df_filtered_signals["reason"] == ""]
ax.scatter(accepted["timestamp"], accepted["close"], color="green", label="Signal accepté", marker="o")

# Signaux rejetés
rejected = df_filtered_signals[df_filtered_signals["reason"] != ""]
ax.scatter(rejected["timestamp"], rejected["close"], color="gray", label="Signal rejeté", marker="x")

# Annotations des raisons
for i, row in rejected.iterrows():
    ax.annotate(row["reason"], (row["timestamp"], row["close"]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color='purple')

ax.set_title("Signaux filtrés – News & Turbulence")
ax.set_xlabel("Date")
ax.set_ylabel("Prix")
ax.legend()
ax.grid(True)

st.pyplot(fig)

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

st.subheader("📊 Visualisation stratégique")

fig, ax = plt.subplots(figsize=(12, 6))

# === Chandeliers japonais ===
candles = df_filtered_signals.copy()
candles["color"] = np.where(candles["close"] >= candles["open"], "green", "red")
for i, row in candles.iterrows():
    ax.plot([row["timestamp"], row["timestamp"]], [row["low"], row["high"]], color="black", linewidth=0.5)
    ax.add_patch(plt.Rectangle(
        (row["timestamp"], min(row["open"], row["close"])),
        width=pd.Timedelta(minutes=30),
        height=abs(row["close"] - row["open"]),
        color=row["color"]
    ))

    if st.checkbox("🕒 Afficher les sessions"):
        for i, row in df_filtered_signals.iterrows():
            color = get_session_color(row["timestamp"].hour)
            ax.axvspan(row["timestamp"] - pd.Timedelta(minutes=15),
                       row["timestamp"] + pd.Timedelta(minutes=15),
                       color=color, alpha=0.2)

if st.checkbox("📊 Afficher les volumes Up/Down"):
    volume_colors = np.where(df_filtered_signals["close"] >= df_filtered_signals["open"], "green", "red")
    ax2 = ax.twinx()
    ax2.bar(df_filtered_signals["timestamp"], df_filtered_signals["volume"], color=volume_colors, alpha=0.3, width=0.02)
    ax2.set_ylabel("Volume", color="gray")
    ax2.tick_params(axis='y', labelcolor='gray')

    if st.checkbox("📍 Afficher les pivots Ballistic"):
        for label, level in pivots.items():
            ax.axhline(y=level, linestyle="--", color="orange", alpha=0.6)
            ax.text(df_filtered_signals["timestamp"].iloc[-1], level, label, color="orange", fontsize=8, ha='right')


# === SL / TP ===
if "SL" in df_filtered_signals.columns and "TP" in df_filtered_signals.columns:
    ax.plot(df_filtered_signals["timestamp"], df_filtered_signals["SL"], linestyle="--", color="gray", label="Stop Loss")
    ax.plot(df_filtered_signals["timestamp"], df_filtered_signals["TP"], linestyle="--", color="purple", label="Take Profit")

# === Signaux filtrés ===
accepted = df_filtered_signals[df_filtered_signals["reason"] == ""]
rejected = df_filtered_signals[df_filtered_signals["reason"] != ""]

ax.scatter(accepted["timestamp"], accepted["close"], color="green", label="Signal accepté", marker="o")
ax.scatter(rejected["timestamp"], rejected["close"], color="gray", label="Signal rejeté", marker="x")

pivots = calculate_ut_pivots(df_filtered_signals)

# === EMA 7x ===
if st.checkbox("📈 Afficher le ruban EMA 7x"):
    for period in ema_periods:
        style = {"linewidth": 2.5} if period == 114 else {"linewidth": 1, "alpha": 0.5}
        ax.plot(df_filtered_signals["timestamp"], df_filtered_signals[f"EMA_{period}"], label=f"EMA {period}", **style)

# === Mise en forme ===
ax.set_title("Graphe stratégique – Chandeliers + SL/TP + EMA 7x")
ax.set_xlabel("Date")
ax.set_ylabel("Prix")
ax.legend()
ax.grid(True)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m %Hh'))
fig.autofmt_xdate()

st.pyplot(fig)

def get_session_color(hour):
    if 0 <= hour < 7:
        return "#e0f7fa"  # Asie – bleu clair
    elif 7 <= hour < 13:
        return "#fff3e0"  # Londres – orange pâle
    elif 13 <= hour < 22:
        return "#e8f5e9"  # New York – vert pâle
    else:
        return "#f5f5f5"  # Off – gris pâle

# Affichage des signaux calculés en fonction des pivots musicaux et de l’EMA 114.
df_signals = generate_signals(df_filtered_signals, pivots=pivots_named)

if st.checkbox("🎼 Afficher les niveaux de partition musicale"):
    for name, value in pivots_named.items():
        st.write(f"{name} : {value:.2f}")

if st.checkbox("📌 Afficher les signaux générés par le moteur"):
    buy_signals = df_signals[df_signals["BuySignal"]]
    sell_signals = df_signals[df_signals["SellSignal"]]

    ax.scatter(buy_signals["timestamp"], buy_signals["close"], color="blue", label="Buy Signal", marker="^")
    ax.scatter(sell_signals["timestamp"], sell_signals["close"], color="red", label="Sell Signal", marker="v")

if st.checkbox("⚡ Afficher l’énergie Ballistic"):
    df_energy, report = grid_search_energy(df_filtered_signals)
    st.write(f"Corrélation énergie vs référence : {report['corr']:.2f}")
    plot_energy_histogram(df_energy)

# Renommage des niveaux de pivots
pivots = calculate_ut_pivots(df_filtered_signals)
pivots_named = rename_pivot_levels(pivots)

# === Affichage des signaux Energie ===
df_energy_signals = generate_energy_signals(df_filtered_signals)

if st.checkbox("⚡ Afficher les signaux énergie"):
    buy_energy = df_energy_signals[df_energy_signals["BuyEnergy"]]
    sell_energy = df_energy_signals[df_energy_signals["SellEnergy"]]

    ax.scatter(buy_energy["timestamp"], buy_energy["CLOSE"], color="lime", label="Buy Énergie", marker="^")
    ax.scatter(sell_energy["timestamp"], sell_energy["CLOSE"], color="darkred", label="Sell Énergie", marker="v")

# === Affichage des signaux combinés Pivots +  Energie + ATR ===
df_combined = generate_combined_signals(df_filtered_signals)

if st.checkbox("🔀 Afficher les signaux combinés (Pivots + Énergie + ATR)"):
    buy_combined = df_combined[df_combined["BuyCombined"]]
    sell_combined = df_combined[df_combined["SellCombined"]]

    ax.scatter(buy_combined["timestamp"], buy_combined["close"], color="gold", label="Buy Convergent", marker="^")
    ax.scatter(sell_combined["timestamp"], sell_combined["close"], color="black", label="Sell Convergent", marker="v")

# Calcul des bornes de la session asiatique (0h–7h UTC)
df_asia = df_filtered_signals[df_filtered_signals["timestamp"].dt.hour.between(0, 6)]
asian_high = df_asia["high"].max()
asian_low = df_asia["low"].min()

# Affichage les trades convergents avec entrées/sorties
import os
os.makedirs("data/logs", exist_ok=True)
df_combined.to_csv("data/logs/combined_signals_log.csv", index=False)

if st.checkbox("📊 Afficher les trades convergents avec entrées/sorties"):
    entries = df_combined[df_combined["TradeType"].notna()]
    exits = df_combined[df_combined["ExitTime"].notna()]

    ax.scatter(entries["timestamp"], entries["close"], color="gold", label="Entrée", marker="^")
    ax.scatter(exits["timestamp"], exits["close"], color="black", label="Sortie", marker="v")

# Optimisation des paramètres du moteur
if st.checkbox("🧪 Optimiser les paramètres du moteur"):
    param_grid = {
        "ema_period": [95, 114, 133],
        "cog_length": [14, 19, 38],
        "atr_mult": [1.5, 2.0, 2.5],
        "energy_threshold": [0.0, 0.2, 0.5]
    }
    df_results = optimize_parameters(df_filtered_signals, param_grid)
    st.dataframe(df_results.sort_values("Sharpe simplifié", ascending=False).head(10))
    df_results.to_csv("data/logs/optimization_results.csv", index=False)

# === Module export journal de trading + calcul de performance ===
trades, summary = summarize_trades(df_combined, pivots=pivots, asian_high=asian_high, asian_low=asian_low)
st.write("📘 Résumé des trades convergents :", summary)
trades.to_csv("data/logs/trade_journal.csv", index=False)

# === 📓 Journal personnel des signaux
# 🔗 Interface de partage pédagogique
st.subheader("🔗 Partage pédagogique")

share_mode = st.selectbox("📡 Mode de partage", ["Copier", "Envoyer à un mentor", "Archiver dans mon journal"])


# === Module filtrage des signaux convergents selon le sentiment des news ===
df_filtered_sentiment = filter_signals_by_sentiment(df_combined, df_news)

if st.checkbox("🧠 Filtrer les signaux convergents selon le ton des news"):
    df_filtered_sentiment = df_filtered_sentiment[df_filtered_sentiment["SentimentFiltered"]]
    st.dataframe(df_filtered_sentiment[["timestamp", "close", "BuyCombined", "SellCombined", "SentimentFiltered"]])

# === Module prédiction de signal ===
# Entraînement du modèle
model_info = train_signal_predictor(trades)
st.write(f"📈 Précision du modèle de prédiction : {model_info['accuracy']:.2f}")

# Exemple de prédiction
if st.checkbox("🔮 Tester une prédiction de signal"):
    hour = st.slider("Heure d'entrée", 0, 23, 9)
    energy = st.slider("Énergie à l'entrée", -2.0, 2.0, 0.5)
    duration = st.slider("Durée estimée (min)", 1, 120, 30)

    prob = predict_signal(model_info["model"], hour, energy, duration)
    st.write(f"Probabilité de réussite du signal : {prob:.2f}")

# === Module détection de tendance ===
df_trend = detect_trend(df_filtered_signals)

if st.checkbox("📈 Afficher la tendance détectée"):
    st.line_chart(df_trend[["TrendCode"]])

# === Module gestion des positions ===
df_positions = compute_position_parameters(df_combined)

if st.checkbox("🎯 Afficher les paramètres de position dynamique"):
    st.dataframe(df_positions[["timestamp", "close", "PositionSize", "StopLoss", "TakeProfit"]])

from modules.backtest_engine import run_backtest

df_backtest = run_backtest(df_positions)

if st.checkbox("📊 Résultats du backtest simulé"):
    st.dataframe(df_backtest[["timestamp", "Direction", "Entry", "Exit", "PnL", "Equity", "Outcome"]])

from modules.trading_api import execute_signals
# === Module exécution des signaux API de trading ===
df_orders = execute_signals(df_positions)

if st.checkbox("🚀 Ordres envoyés via API simulée"):
    st.dataframe(df_orders)

from docs.generate_docs import get_module_docs
# === Module documentation pédagogique ===
if st.checkbox("📚 Documentation pédagogique du bot"):
    docs = get_module_docs()
    for section, items in docs.items():
        st.subheader(section)
        for item in items:
            st.markdown(f"- {item}")

from modules.scanner_intraday import scan_eligible_assets
# === Module scanner intraday ===
asset_data = {
    "EURUSD": df_eurusd,
    "GBPUSD": df_gbpusd,
    "XAUUSD": df_xauusd
}

if st.checkbox("🔍 Scanner les actifs intraday éligibles"):
    eligible_assets = scan_eligible_assets(
        asset_data,
        signal_reference=df_filtered_signals,
        min_volatility=0.4,
        min_volume=80000,
        trend_filter=True,
        range_filter=False,
        news_filter=df_news
    )
    st.write("Actifs éligibles à la prise de position :")
    for asset in eligible_assets:
        st.markdown(f"- **{asset['symbol']}** | Vol : {asset['volatility']} | Volu : {asset['volume']} | Corr : {asset['correlation']} | News : {asset['news']} | Tendance : {asset['trend']}")

# Appel du compte propfirm optimal
best_account = select_best_account(accounts_df, strategy_mode="intraday", require_constance=False)

from modules.account_selector import select_best_account
# Appel du module de compte propfirm optimal
accounts_df = pd.read_csv("data/propfirm_accounts.csv")

if st.checkbox("🏦 Sélectionner le compte propfirm optimal"):
    best_account = select_best_account(accounts_df, strategy_type="swing", allow_overnight=True, require_constance=False)
    st.write("Compte recommandé :")
    st.dataframe(best_account)

from modules.account_router import route_signals_to_accounts
# Appel du module de routage des signaux
accounts_df = pd.read_csv("data/propfirm_accounts.csv")
df_routed = route_signals_to_accounts(df_combined, accounts_df)

if st.checkbox("🧭 Routage des signaux vers les comptes propfirm"):
    st.dataframe(df_routed[["timestamp", "close", "BuyCombined", "SellCombined", "AssignedAccount"]])

from modules.performance_dashboard import analyze_performance
# Appel du module de performances du bot
if st.checkbox("📊 Analyse des performances du bot"):
    perf = analyze_performance(trades)
    for k, v in perf.items():
        st.write(f"**{k}** : {v}")

from modules.quantum_bridge import simulate_quantum_execution
# Appel du module de simulation d’envoi d’ordres vers Quantum
df_quantum_orders = simulate_quantum_execution(df_routed)

if st.checkbox("🛰️ Passerelle simulée vers Quantum"):
    st.dataframe(df_quantum_orders[["order_id", "timestamp", "symbol", "side", "size", "entry_price", "stop_loss", "take_profit", "strategy", "status"]])

from modules.multi_timeframe_convergence import detect_convergence
# Appel du module de signal sur plusieurs unités de temps
df_converged = detect_convergence(df_m1, df_m5, df_m15)

if st.checkbox("📐 Signaux en convergence multi-timeframe"):
    st.dataframe(df_converged[["timestamp"]])

from modules.volatility_clustering import detect_volatility_clusters
# Appel du module de détection de volatilité
df_vol_clustered = detect_volatility_clusters(df_combined)

if st.checkbox("🌪️ Lecture des clusters de volatilité"):
    st.dataframe(df_vol_clustered[["timestamp", "Volatility", "VolatilityCluster"]])

from modules.liquidity_zones import detect_liquidity_zones
# Appel du module d'identification des zones de liquidité
df_liquidity = detect_liquidity_zones(df_combined)

if st.checkbox("💧 Lecture des zones de liquidité"):
    st.dataframe(df_liquidity[["timestamp", "MidPrice", "LiquidityZone"]])

from modules.orderflow_reader import analyze_orderflow
# Appel du module de lecture du carnet d'ordres.
df_orderflow = analyze_orderflow(df_combined)

if st.checkbox("📊 Lecture de l’orderflow et des déséquilibres"):
    st.dataframe(df_orderflow[["timestamp", "AggressionType", "Imbalance", "Absorption"]])

from modules.signal_attribution import attribute_signals
# Appel du module de traçabilité des signaux
df_attributed = attribute_signals(df_combined)

if st.checkbox("🧬 Attribution des signaux par module"):
    st.dataframe(df_attributed[["timestamp", "BuyCombined", "SellCombined", "SignalSource"]])

from modules.propfirm_compatibility_checker import check_signal_compatibility
# Appel du module de filtrage des signaux autorisés ou bloqués
rules_df = pd.read_csv("data/propfirm_rules.csv")
df_checked = check_signal_compatibility(df_combined, rules_df)

if st.checkbox("🛡️ Vérification de compatibilité propfirm"):
    st.dataframe(df_checked[["timestamp", "BuyCombined", "SellCombined", "Compatible", "Reason"]])

from modules.explainable_ai import explain_signal
# Appel du module d'explication claire pour chaque signal
df_explained = df_combined.copy()
df_explained["Explanation"] = df_explained.apply(explain_signal, axis=1)

if st.checkbox("🧠 Explication pédagogique des signaux"):
    st.dataframe(df_explained[["timestamp", "BuyCombined", "SellCombined", "Explanation"]])

from modules.replay_mode import replay_signals
# Appel du module de lecture séquentielle des signaux
if st.checkbox("🎬 Rejouer une journée de signaux"):
    replay_msgs = replay_signals(df_attributed, speed=0.1)
    for msg in replay_msgs:
        st.markdown(f"- {msg}")

from modules.scenario_builder import build_scenario
# Appel du module de simulation ciblée
scenario_type = st.selectbox("🎭 Choisir un scénario pédagogique", ["breakout", "range", "news_spike", "reversal"])
df_scenario = build_scenario(df_combined, scenario_type)

if st.checkbox("🧪 Afficher les signaux du scénario choisi"):
    st.dataframe(df_scenario[["timestamp", "close", "ScenarioType"]])

# 🧠 Liaison de la simulation au score de confiance et aux alertes pédagogiques
def comment_simulation(row):
    score = row.get("ConfidenceScore", 5)
    if score >= 8:
        return "🧠 Signal fort : la simulation montre un bon ratio risque/rendement."
    elif score <= 3:
        return "⚠️ Signal faible : prudence, le risque semble élevé par rapport au gain potentiel."
    return "ℹ️ Signal moyen : à surveiller, ajuster les paramètres si nécessaire."

# Exemple d'application sur le signal sélectionné
selected_signal = df_validated.iloc[0]  # ou via selectbox
st.markdown(comment_simulation(selected_signal))

from modules.structure_tracker import track_structure
# Appel du module de lecture dynamique du marché
df_structured = track_structure(df_combined)

if st.checkbox("📐 Lecture de structure SMC (HH/HL, BOS, ChOCh)"):
    st.dataframe(df_structured[["timestamp", "StructureType", "BOS", "ChOCh"]])

from modules.zigzag_mapper import map_zigzag
# Appel du module de zig zag intelligent
zigzag_df = map_zigzag(df_combined)

if st.checkbox("📈 Tracer le zigzag structurel"):
    st.dataframe(zigzag_df)

from modules.order_blocks import detect_order_blocks
# Appel du module d'identification des zones institutionnelles
df_ob = detect_order_blocks(df_combined)

if st.checkbox("🏛️ Détection des Order Blocks institutionnels"):
    st.dataframe(df_ob[["timestamp", "OBType", "close"]])

from modules.fvg_detector import detect_fvg
# Appel du module de détection des déséquilibres
df_fvg = detect_fvg(df_combined)

if st.checkbox("📉 Détection des Fair Value Gaps (FVG)"):
    st.dataframe(df_fvg[["timestamp", "FVGType", "low", "high"]])

from modules.mitigation_mapper import map_mitigation
# Appel du module de détection des comblements
df_mitigated = map_mitigation(df_combined, df_fvg)

if st.checkbox("🩹 Détection des retours sur zones (Mitigation)"):
    st.dataframe(df_mitigated[["timestamp", "close", "Mitigated"]])

from modules.poi_mapper import map_poi
# Appel du module d'identification des zones à surveiller
df_poi = map_poi(df_combined)

if st.checkbox("🎯 Affichage des Points of Interest (POI)"):
    st.dataframe(df_poi[["timestamp", "POI"]])

from modules.multi_tf_contextualizer import contextualize_signal
# Appel du module de lecture multi timefranes de structure de marché
df_contextualized = contextualize_signal(df_m1, df_m5, df_m15)

if st.checkbox("🧭 Contexte multi-timeframe des signaux"):
    st.dataframe(df_contextualized[["timestamp", "BuyCombined", "SellCombined", "M5_Context", "M15_Context"]])

from modules.signature_generator import render_signature
# Appel du module de signature visuelle
signature_mode = st.selectbox("🎨 Choisir la signature visuelle", ["symbolic", "minimal", "none"])
render_signature(signature_mode)

from modules.packaging_module import prepare_packaging
# Appel du module de diffusion
package_config = prepare_packaging(mode="educational", include_dashboard=True)
st.json(package_config)

# Poucentage seuil Risk/Reward
rr_threshold = st.slider("🎚️ Risk/Reward Ratio", 0.5, 5.0, 2.0, 0.1)
st.markdown(f"📈 Ratio sélectionné : {rr_threshold:.1f} : 1")
st.markdown(parameter_guidance["RiskReward"])

if rr_threshold > 4.0 and structure_choice == "range":
    st.warning("⚠️ Ratio élevé en contexte de range : probabilité d’entrée faible, risque de faux signal.")

scenario = {
    "name": "Filtrage par gain optimal",
    "type": "gain_filter",
    "conditions": [
        "SignalSuccess == 1",
        f"RiskReward > {rr_threshold}"
    ],
    "expected": "high_expectancy"
}

# Mode “auto-pédagogique”
if st.checkbox("🤖 Laisser le bot choisir le scénario optimal"):
    scenario = bot_select_best_scenario(df)
    st.markdown(f"🧠 Scénario choisi : {scenario['name']}")
    st.markdown(f"📚 Justification : {scenario['expected']}")

auto_mode = st.checkbox("🤖 Laisser le bot choisir le scénario optimal")

if auto_mode:
    scenario = bot_select_best_scenario(df)
    st.markdown(f"🧠 Scénario choisi : {scenario['name']}")
    st.markdown(f"📚 Justification : {scenario['expected']}")

# 🧑‍🏫 Appel de validation mentorale avant réactivation
st.subheader("🧑‍🏫 Demande de réactivation mentorale")

scenario = st.selectbox("🎭 Scénario désactivé", memory_df[memory_df["IsActive"] == False]["ScenarioType"])
mentor = st.text_input("👤 Nom du mentor")
comment = st.text_area("📝 Justification", height=100)

if st.button("📨 Soumettre la demande"):
    request_mentor_validation(scenario, mentor, comment)
    st.success("✅ Demande envoyée au mentor.")

def bot_select_best_scenario(df):
    best = None
    max_score = -float("inf")

    for name, sc in scenarios.items():
        temp = validate_scenario(df, sc)
        if temp.empty:
            continue

        rr_avg = temp["RiskReward"].mean() if "RiskReward" in temp else 0
        vol_avg = temp["Volume"].mean() if "Volume" in temp else 0
        mitigated_ratio = temp["Mitigated"].mean() if "Mitigated" in temp else 0
        structure = sc.get("type", "")

        # Score brut
        score = len(temp) + rr_avg + (vol_avg / 1000) + mitigated_ratio

        # Pénalité douce via mémoire
        penalty = 0
        for error in memory_log:
            if error.get("StructureType") == structure and error.get("RiskReward", 0) > 4.0:
                penalty += 0.5

        score -= penalty

        if score > max_score:
            best = sc.copy()
            best["name"] = name
            max_score = score

    return best

    # Exemple : extraire les paramètres du signal le plus fort
    best_signal = df_validated.sort_values("ConfidenceScore", ascending=False).iloc[0]

    entry_price = best_signal["entry_price"] if "entry_price" in best_signal else 100.0
    stop_loss = best_signal["stop_loss"] if "stop_loss" in best_signal else entry_price - 5
    take_profit = best_signal["take_profit"] if "take_profit" in best_signal else entry_price + 10

# 🧠 Mémoire évolutive du bot
def update_bot_memory(df_validated):
    """
    Enregistre les erreurs ou signaux rejetés pour apprentissage futur.
    """
    errors = df_validated[df_validated["SignalSuccess"] == 0]
    # Ici tu peux stocker les erreurs dans un fichier, une base, ou une variable persistante
    return errors

# Enrichissement du dashboard
def assign_signal_type(row):
    if row.get("BOS") and row.get("FVGType") == "bullish" and row.get("OrderBlock"):
        return "BuyCombined"
    elif row.get("ChOCh") and row.get("FVGType") == "bearish" and not row.get("Mitigated"):
        return "SellCombined"
    return "Neutral"

# 🔧 Alertes pédagogiques dynamiques
with st.expander("🧠 Conseils pédagogiques du Professeur"):
    st.markdown(suggest_adjustment(rr_threshold, structure_choice))
    st.markdown(suggest_volume(volume_threshold))
    st.markdown(suggest_mitigation(mitigation_filter))

    # Visualisation graphique du score de confiance
    st.subheader("📊 Score de confiance des signaux")
    st.bar_chart(df_validated["ConfidenceScore"])

    # 🧠 Visualisation pédagogique par scénario
    st.subheader("📊 Répartition des signaux par type")
    signal_counts = df_validated["SignalType"].value_counts()
    st.bar_chart(signal_counts)

    # 🧠 Visualisation pédagogique par type de signal
    st.subheader("📊 Répartition des signaux par scénario")
    scenario_counts = df_validated["ScenarioType"].value_counts()
    st.bar_chart(scenario_counts)

    # 🔧 Selectbox de visualisation pédagogique  pour interface adaptative
    view_mode = st.selectbox("🎛️ Vue pédagogique", ["Par type de signal", "Par scénario"])

    if view_mode == "Par type de signal":
        st.bar_chart(df_validated["SignalType"].value_counts())
    else:
        st.bar_chart(df_validated["ScenarioType"].value_counts())
        
    # Affichage du signal lumineux Live du Professeur
    st.subheader("🔦 Signal lumineux du Professeur")
    for _, row in df_validated.iterrows():
        st.markdown(f"{row['timestamp']} → {row['LiveSignal']}")

    with st.expander("🔦 Signal lumineux du Professeur"):
        for _, row in df_validated.iterrows():
            st.markdown(f"{row['timestamp']} → {row['LiveSignal']}")
    
    # Clarification des signaux lumineux vs sens de position
        st.markdown(f"🔦 Signal : {row['LiveSignal']} — 📈 Sens : {row['SignalType']}")

    with st.expander("📘 Légende des signaux"):
        st.markdown("🟢 = Entrée recommandée\n🟠 = À surveiller\n🔴 = Sortie suggérée\n⚫ = Signal périmé")
        st.markdown("📈 BuyCombined = signal haussier\n📉 SellCombined = signal baissier")

    # 🧠 Affichage liaison de la simulation au score de confiance et aux alertes pédagogiques
        st.markdown(f"📈 Signal : {selected_signal['SignalType']}")
        st.markdown(f"🔦 Niveau : {selected_signal['LiveSignal']}")
        st.markdown(f"🎯 Score de confiance : {selected_signal['ConfidenceScore']}/10")

# 📤 Export pédagogique pour documentation, partage ou archivage.
st.subheader("📤 Export pédagogique")

export_text = f"""
🧠 Signal : {selected_signal['SignalType']}
🔦 Niveau : {selected_signal['LiveSignal']}
🎯 Score de confiance : {selected_signal['ConfidenceScore']}/10
📌 Taille de position : {position_units:.2f} unités
📈 Gain potentiel : {reward:.2f} $
📉 Risque engagé : {risk_amount:.2f} $
🗒️ Commentaire : {comment_simulation(selected_signal)}
"""

st.text_area("📝 Résumé exportable", value=export_text, height=200)

# 💬 Module de feedback utilisateur
    st.subheader("💬 Feedback utilisateur")

    feedback = st.text_area("🗣️ Que pensez-vous de ce signal ou de cette simulation ?", height=100)
    if st.button("📨 Envoyer le feedback"):
        st.success("✅ Merci pour votre retour ! Il sera pris en compte dans l'évolution du Professeur.")
        # Option : enregistrer dans un fichier ou base

from modules.signal_filter import auto_deactivate_signals
# Chargement des feedbacks
feedback_df = pd.read_csv("utils/feedback_log.txt", sep="|", names=["timestamp", "feedback", "decision"])

# Mise à jour des signaux
df_validated = auto_deactivate_signals(df_validated, feedback_df, threshold=3)


# 🔗 Interface de partage pédagogique
st.subheader("🔗 Partage pédagogique")

share_mode = st.selectbox("📡 Mode de partage", ["Copier", "Envoyer à un mentor", "Archiver dans mon journal"])
if share_mode == "Copier":
    st.markdown("📋 Copiez le résumé ci-dessus et collez-le où vous voulez.")
elif share_mode == "Envoyer à un mentor":
    st.markdown("📨 Fonction d'envoi à venir (email/API).")
elif share_mode == "Archiver dans mon journal":
    st.markdown("🗂️ Fonction d'archivage local à venir.")

# ✅ Module de validation mentorale
st.subheader("✅ Validation mentorale")

decision = st.selectbox("🧠 Décision du mentor", ["Valider", "Rejeter", "À revoir"])
mentor_feedback = st.text_area("📝 Commentaire du mentor", height=100)

if st.button("📨 Enregistrer la validation"):
    validate_signal(selected_signal["timestamp"], decision, mentor_feedback)
    st.success("✅ Validation enregistrée.")



st.dataframe(df_validated.filter(items=["timestamp", "ScenarioType", "ExpectedOutcome", "Explanation", "ConfidenceScore"], axis=1, errors="ignore"))

# 🔧 Suggestions pédagogiques dynamiques pour volume
def suggest_volume(volume):
    if volume < vol_q1:
        return "📉 Volume faible : risque de faux signal."
    elif volume > vol_q3:
        return "📈 Volume élevé : possible impulsion ou réveil de session."
    return "✅ Volume dans la moyenne."


# 🔧 Suggestions pédagogiques pour mitigation
def suggest_mitigation(mitigation):
    if mitigation == "Mitigated":
        return "🧠 Signal mitigé : plus fiable mais souvent plus tardif."
    elif mitigation == "Non mitigated":
        return "⚠️ Signal brut : plus rapide mais plus risqué sans confirmation."
    return "ℹ️ Tous les signaux sont pris en compte, mitigés ou non."

# 🔧 Fonction score de confiance de 0 à 10
def compute_confidence_score(row):
    score = 5  # point de départ neutre

    if row.get("RiskReward", 0) >= 2.0:
        score += 2
    elif row.get("RiskReward", 0) < 1.0:
        score -= 2

    if row.get("Volume", 0) > 3000:
        score += 1
    elif row.get("Volume", 0) < 500:
        score -= 1

    if row.get("Mitigated") is True:
        score += 1
    elif row.get("Mitigated") is False:
        score -= 1

    if row.get("StructureType") == "range" and row.get("RiskReward", 0) > 4.0:
        score -= 2  # piège typique

    return max(0, min(10, score))

    # Couleur bande centrale UT Pivots
    if row.get("PivotBias") == "bullish":
        score += 1
    elif row.get("PivotBias") == "bearish":
        score -= 1

    # Intégration phoebus Energie et UT Pivots dans le score de confiance
    if row.get("EnergyLevel") == "high":
        score += 1
    elif row.get("EnergyLevel") == "low":
        score -= 1

    if row.get("PivotBias") == "bullish" and row.get("SignalType") == "BuyCombined":
        score += 1
    elif row.get("PivotBias") == "bearish" and row.get("SignalType") == "SellCombined":
        score += 1

# ✅ Définition du signal lumineux pour le mode Live
def live_professor_signal(row):
    if row["ConfidenceScore"] >= 8 and row["SignalType"] in ["BuyCombined", "SellCombined"]:
        return "🟢 Entrée recommandée"
    elif row["ConfidenceScore"] <= 3:
        return "🔴 Entrée déconseillée"
    return "🟡 À surveiller"

from datetime import datetime, timedelta
# 🟢🟠🔴⚫ Interface “live du Professeur” — 4 signaux lumineux
def live_professor_signal(row, now=None):
    now = now or datetime.utcnow()
    ts = pd.to_datetime(row.get("timestamp"))
    age = (now - ts).total_seconds() / 60  # minutes

    if age > 60:
        return "⚫ Signal périmé"
    if row["ConfidenceScore"] >= 8:
        return "🟢 Entrée recommandée"
    elif row["ConfidenceScore"] <= 3:
        return "🔴 Sortie suggérée"
    return "🟠 Entrée à surveiller"

# 📈 Appel du score adaptatif en direct
df_validated["AdjustedScore"] = df_validated.apply(
    lambda row: adapt_confidence_score(row["ConfidenceScore"], row["ScenarioType"], memory_dict),
    axis=1
)

# ⏱️ Module de gestion du timing des signaux lumineux
def is_signal_expired(row, now=None, max_age_minutes=60):
    now = now or datetime.utcnow()
    ts = pd.to_datetime(row.get("timestamp"))
    return (now - ts).total_seconds() > max_age_minutes * 60

# 💼 Menu déroulant du module de money management
st.subheader("💼 Paramètres de gestion du risque")

account_size = st.number_input("💰 Taille du compte ($)", min_value=100, value=10000, step=100)
risk_per_trade = st.slider("📉 Risque par trade (%)", 0.1, 5.0, 1.0, 0.1)
max_drawdown = st.slider("📉 Drawdown maximal autorisé (%)", 1.0, 20.0, 10.0, 0.5)
stop_loss_mode = st.selectbox("🛑 Mode de stop-loss", ["Fixe", "Volatilité", "Structure"])

position_size = (account_size * (risk_per_trade / 100))  # simplifié
st.markdown(f"📌 Taille de position suggérée : **{position_size:.2f} $**")

# 💼 Simulation de money management — amorce pédagogique
st.subheader("🧪 Simulation de gestion du risque")

    # 🧠 Le signal sélectionné pré-remplit les champs de simulation.
entry_price = selected_signal.get("entry_price", 100.0)
stop_loss = selected_signal.get("stop_loss", entry_price - 5)
take_profit = selected_signal.get("take_profit", entry_price + 10)

entry_price = st.number_input("🎯 Prix d'entrée", value=entry_price)
stop_loss = st.number_input("🛑 Stop-loss", value=stop_loss)
take_profit = st.number_input("🎯 Take-profit", value=take_profit)


entry_price = st.number_input("🎯 Prix d'entrée", min_value=0.0, value=100.0)
stop_loss = st.number_input("🛑 Stop-loss", min_value=0.0, value=95.0)
take_profit = st.number_input("🎯 Take-profit", min_value=0.0, value=110.0)

risk_amount = account_size * (risk_per_trade / 100)
risk_per_unit = abs(entry_price - stop_loss)
position_units = risk_amount / risk_per_unit if risk_per_unit else 0
reward = abs(take_profit - entry_price) * position_units

st.markdown(f"📌 Taille de position : **{position_units:.2f} unités**")
st.markdown(f"📈 Gain potentiel : **{reward:.2f} $**")
st.markdown(f"📉 Risque engagé : **{risk_amount:.2f} $**")

# ✅ Appel mémoire locale (journal de feedback)
if st.button("📨 Envoyer le feedback"):
    save_feedback(selected_signal["timestamp"], feedback)
    st.success("✅ Merci pour votre retour !")

# 🧑‍🏫 Interface mentor-élève
st.subheader("🧑‍🏫 Interface mentor-élève")

mentor_comment = st.text_area("📣 Commentaire du mentor", height=100)
if st.button("📨 Envoyer au mentor"):
    save_mentor_comment(selected_signal["timestamp"], mentor_comment)
    st.success("✅ Signal envoyé au mentor. En attente de retour.")

# 🧑‍🏫 2. Interface mentorale multi-utilisateur
st.subheader("🧑‍🏫 Validation par mentor")

mentor_name = st.text_input("👤 Nom du mentor")
decision = st.selectbox("🧠 Décision", ["Valider", "Rejeter", "À revoir"])
comment = st.text_area("📝 Commentaire", height=100)

if st.button("📨 Enregistrer la validation"):
    save_mentor_feedback("user_001", selected_signal["timestamp"], mentor_name, decision, comment)
    st.success("✅ Validation enregistrée.")

# 🔔 Interface de notification pour les validations
st.subheader("🔔 Notifications mentorales")

notifications = load_user_notifications("user_001")
for note in notifications:
    st.markdown(f"📬 {note['timestamp']} — {note['message']}")
    #👉 Tu peux stocker les notifications dans utils/notifications.txt

# 🚦 4. Filtrage des signaux actifs/inactifs selon contexte
df_filtered = df_validated[df_validated["is_active"] == True]

# 📈 Score adaptatif en direct
from modules.memory_evolution import apply_memory_to_score

df_validated["AdjustedScore"] = df_validated.apply(
    lambda row: apply_memory_to_score(row["ConfidenceScore"], row["ScenarioType"], memory_dict),
    axis=1
)

st.subheader("📊 Score de confiance ajusté")
st.bar_chart(df_validated["AdjustedScore"])

# Appel de validation mentorale avant réactivation
st.subheader("🧑‍🏫 Demande de réactivation mentorale")

scenario = st.selectbox("🎭 Scénario désactivé", memory_df[memory_df["IsActive"] == False]["ScenarioType"])
mentor = st.text_input("👤 Nom du mentor")
comment = st.text_area("📝 Justification", height=100)

if st.button("📨 Soumettre la demande"):
    request_mentor_validation(scenario, mentor, comment)
    st.success("✅ Demande envoyée au mentor.")

from modules.auto_mentor import auto_mentor_feedback
✅ Appel pré-validation automatique sans mentor
st.subheader("🤖 Pré-validation automatique du Professeur")

df_validated["AutoDecision"] = df_validated.apply(
    lambda row: auto_mentor_feedback(row)[0], axis=1
)
df_validated["AutoComment"] = df_validated.apply(
    lambda row: auto_mentor_feedback(row)[1], axis=1
)

st.dataframe(df_validated[["ScenarioType", "ConfidenceScore", "AutoDecision", "AutoComment"]])

# 📊 Génération de dashboard.py en CLI avec un prototype simple et lisible :
# dashboard.py
import os
from config_loader import load_all_configs

def show_dashboard():
    configs = load_all_configs()
    print("\n📊 DASHBOARD — Private Assistant\n")

    # Lecture des derniers exports
    for module in ["core_analysis", "execution_engine", "propfirm_guard", "pedagogical_output"]:
        path = f"exports/{module}_export.csv"
        if os.path.exists(path):
            print(f"✅ {module} : export disponible")
        else:
            print(f"❌ {module} : export absent")

    # Lecture des replays
    print("\n📂 Replays disponibles :")
    for f in os.listdir("replays"):
        if f.endswith(".txt") or f.endswith(".md"):
            print(f" - {f}")

    # Lecture du log global
    log_path = "exports/global_test_log.csv"
    if os.path.exists(log_path):
        print("\n📄 Log global : présent")
    else:
        print("\n📄 Log global : absent")

if __name__ == "__main__":
    show_dashboard()

# ✅ Bouton “Ouvrir visualiseur des liens” dans le dashboard principal
st.header("🔗 Accès aux liens du projet")

if st.button("📋 Ouvrir le visualiseur des liens"):
    st.markdown("➡️ Navigue dans le menu latéral à gauche : **🔗 Liens du projet**")
    st.info("Ou place le fichier dans `/pages/` pour l’activer automatiquement.")

# 🌲 Vue arborescente des fichiers dans le dashboard principal
# 💡 Possibilité de restreindre à certains dossiers (config/, utils/, pages/) si besoin.
import os

st.header("🌲 Vue arborescente du projet")

def render_tree(path, level=0):
    for item in sorted(os.listdir(path)):
        full_path = os.path.join(path, item)
        indent = " " * level
        if os.path.isdir(full_path):
            st.markdown(f"{indent}📁 **{item}**")
            render_tree(full_path, level + 1)
        else:
            st.markdown(f"{indent}📄 {item}")

if st.checkbox("📂 Afficher l’arborescence du projet"):
    render_tree(".")

# 🔊 1. Bouton “Lire les liens à voix haute” dans le dashboard
st.header("🔊 Synthèse vocale des liens")

if st.button("📢 Lire les liens à voix haute"):
    import yaml
    import pyttsx3

    with open("config/bot_registry_links.yaml", "r") as f:
        links = yaml.safe_load(f)

    summary = "🔗 Liens et raccourcis du projet :\n"
    for key, meta in links.items():
        summary += f"{meta['label']} : {meta['chemin']}\n"
        if "export_md" in meta:
            summary += f"Export markdown : {meta['export_md']}\n"
        if "capture" in meta:
            summary += f"Capture : {meta['capture']}\n"
        summary += "\n"

    engine = pyttsx3.init()
    engine.say(summary)
    engine.runAndWait()
    st.success("Lecture terminée.")

# 📋 Bouton “Générer résumé vocal .md” dans le dashboard
st.header("📋 Export résumé vocal des liens")

if st.button("📝 Générer bot_registry_links_summary.md"):
    from utils.export_links_summary_md import export_links_summary_md
    export_links_summary_md()
    st.success("✅ Export généré : `bot_registry_links_summary.md`")

# 🔊 Bouton “Ouvrir synthèse vocale” dans le dashboard
st.header("🔉 Synthèse vocale")

if st.button("🎧 Ouvrir la page d’écoute vocale"):
    st.markdown("➡️ Navigue dans le menu latéral à gauche : **🔉 Synthèse Vocale**")
    st.info("Ou place le fichier dans `/pages/` pour l’activer automatiquement.")

# 🎧 Bouton “Générer version MP3” dans le dashboard
st.header("🎙️ Export MP3 pour diffusion externe")

if st.button("🎧 Générer onboarding_links.mp3"):
    from utils.export_links_audio_mp3 import export_links_audio_mp3
    export_links_audio_mp3()
    st.success("✅ Audio MP3 exporté : `onboarding_links.mp3` dans `exports/audio/`")

# 🎙️ Bouton “Ouvrir gestion audio” dans le dashboard
st.header("🎙️ Gestion audio")

if st.button("🎧 Ouvrir la page de gestion audio"):
    st.markdown("➡️ Navigue dans le menu latéral à gauche : **🎙️ Audio Export**")
    st.info("Ou place le fichier dans `/pages/` pour l’activer automatiquement.")

# 🗂️ Bouton “Ouvrir usages vocaux” dans le dashboard
st.header("🗂️ Usages vocaux")

if st.button("🎙️ Ouvrir la page des usages vocaux"):
    st.markdown("➡️ Navigue dans le menu latéral à gauche : **🗂️ Usages Vocaux**")
    st.info("Ou place le fichier dans `/pages/` pour l’activer automatiquement.")

# 🔁 Bouton “Écouter résumé des rôles vocaux” dans le dashboard principal
st.header("🔁 Résumé vocal des rôles")

if st.button("🎙️ Écouter résumé des rôles vocaux"):
    audio_path = "exports/audio/audio_roles_summary.wav"
    if os.path.exists(audio_path):
        st.audio(audio_path, format="audio/wav")
    else:
        st.warning("⚠️ Fichier audio non trouvé.")

# 🧠 Bouton “Ouvrir Synthèse Onboarding” dans le dashboard
st.header("🧠 Synthèse Onboarding")

if st.button("📘 Ouvrir la page Synthèse Onboarding"):
    st.markdown("➡️ Navigue dans le menu latéral à gauche : **🧠 Synthèse Onboarding**")
    st.info("Ou place le fichier dans `/pages/` pour l’activer automatiquement.")

# 🧩 Bouton “Tout exporter (audio + md)” dans le dashboard
st.header("🧩 Export global onboarding")

if st.button("📦 Tout exporter (audio + md)"):
    from utils.export_links_summary_md import export_links_summary_md
    from utils.export_audio_md import export_audio_md
    from utils.export_onboarding_md import export_onboarding_md
    from utils.export_links_audio import export_links_audio
    from utils.export_audio_roles_vocal import export_audio_roles_vocal
    from utils.export_audio_roles_mp3 import export_audio_roles_mp3

    export_links_summary_md()
    export_audio_md()
    export_onboarding_md()
    export_links_audio()
    export_audio_roles_vocal()
    export_audio_roles_mp3()

    st.success("✅ Tous les fichiers audio et markdown ont été exportés dans `exports/`.")

# 🎧 Bouton “Écouter synthèse finale” dans le dashboard principal
st.header("🔊 Synthèse finale")

if st.button("🎧 Écouter synthèse finale du projet"):
    final_audio = "exports/audio/onboarding_final_summary.wav"
    if os.path.exists(final_audio):
        st.audio(final_audio, format="audio/wav")
    else:
        st.warning("⚠️ Fichier audio non trouvé.")

# 📦 Bouton “Ouvrir Export Global” dans le dashboard
st.header("📦 Export Global")

if st.button("📂 Ouvrir la page Export Global"):
    st.markdown("➡️ Navigue dans le menu latéral à gauche : **📦 Export Global**")
    st.info("Tous les fichiers `.md`, `.wav`, `.mp3`, `.yaml` sont listés et consultables.")

# 📁 Bouton “Ouvrir Structure Projet” dans le dashboard
st.header("📁 Structure du projet")

if st.button("🗂️ Ouvrir la page Structure Projet"):
    st.markdown("➡️ Navigue dans le menu latéral à gauche : **📁 Structure Projet**")
    st.info("Visualisation complète des dossiers, fichiers, rôles et usages.")

# 🧾 Bouton “Ouvrir Manifeste Interactif” dans le dashboard
st.header("🧾 Manifeste interactif")

if st.button("📘 Ouvrir la page Manifeste Interactif"):
    st.markdown("➡️ Navigue dans le menu latéral à gauche : **🧾 Manifeste Interactif**")
    st.info("Explore chaque bloc du manifeste versionné.")

# 🎧 Bouton “Écouter version contractuelle (.mp3)” dans le dashboard
st.header("🎧 Version contractuelle (.mp3)")

if st.button("📘 Écouter synthèse contractuelle"):
    mp3_path = "exports/audio/onboarding_manifest_summary.mp3"
    if os.path.exists(mp3_path):
        st.audio(mp3_path, format="audio/mp3")
    else:
        st.warning("⚠️ Fichier MP3 non trouvé.")

# 📘 Bouton “Ouvrir Contrats Vocaux” dans le dashboard
st.header("📘 Contrats vocaux")

if st.button("🔊 Ouvrir la page Contrats Vocaux"):
    st.markdown("➡️ Navigue dans le menu latéral à gauche : **📘 Contrats Vocaux**")
    st.info("Écoute et validation des blocs contractuels.")

# 🔐 Bouton “Valider projet” dans le dashboard principal
st.header("🔐 Verrouillage contractuel")

if st.button("✅ Valider projet"):
    st.success("🧾 Le projet est verrouillé contractuellement. Tous les blocs sont validés et archivés.")
    st.markdown("📘 Consulte la page **Contrats Vocaux** pour réécouter la synthèse finale.")

# 📦 Bouton “Télécharger archive complète” dans le dashboard
st.header("📦 Archive complète")

zip_path = "exports/export_all.zip"
if os.path.exists(zip_path):
    with open(zip_path, "rb") as f:
        st.download_button(
            label="📥 Télécharger l’archive complète",
            data=f,
            file_name="PrivateAssistant_Archive.zip",
            mime="application/zip"
        )
else:
    st.warning("⚠️ Archive ZIP introuvable.")

# 🧾 Bouton “Ouvrir Certification Finale” dans le dashboard
st.header("🧾 Certification finale")

if st.button("📘 Ouvrir la page Certification Finale"):
    st.markdown("➡️ Navigue dans le menu latéral à gauche : **🧾 Certification Finale**")
    st.info("Visualisation des blocs validés et signature de clôture.")

# 📢 Bouton “Ouvrir Diffusion Projet” dans le dashboard
st.header("📢 Diffusion publique")

if st.button("📘 Ouvrir la page Diffusion Projet"):
    st.markdown("➡️ Navigue dans le menu latéral à gauche : **📢 Diffusion Projet**")
    st.info("Partage des blocs publics et synthèses vocales externes.")

# 🌐 Bouton “Ouvrir Partage Externe” dans le dashboard
st.header("🌐 Partage externe")

if st.button("📘 Ouvrir la page Partage Externe"):
    st.markdown("➡️ Navigue dans le menu latéral à gauche : **🌐 Partage Externe**")
    st.info("Accès aux blocs publics et synthèses vocales externes.")

# 🔐 Bouton “Clôture officielle” dans le dashboard
st.header("🔐 Clôture officielle")

if st.button("🚀 Verrouiller le projet"):
    st.success("✅ Clôture officielle enregistrée. Le projet est verrouillé et prêt pour diffusion.")
    st.markdown("📁 Consulte la page **Historique Projet** pour visualiser les validations et soumissions.")
