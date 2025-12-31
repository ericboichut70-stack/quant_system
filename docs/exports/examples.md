# 📤 Exemples d’Exports (`exports/`)

Ce document présente des **exemples concrets** d’exports générés par le moteur quantitatif, les modules avancés et les interfaces.  
Il complète `formats.md` en montrant des cas réels, structurés et immédiatement exploitables.

---

## 🧭 1. Exports CSV

## 1.1 Signaux de Trading

```csv
timestamp,open,high,low,close,volume,buy_signal,sell_signal,ai_score
2024-01-03 09:30,182.1,183.0,181.9,182.7,1203400,1,0,78
2024-01-03 09:35,182.7,183.2,182.5,183.0,980200,0,0,65
2024-01-03 09:40,183.0,183.4,182.8,183.3,1104500,0,1,42

## 1.2 Résultats de Backtest

trade_id,entry_time,exit_time,entry_price,exit_price,pnl,risk_reward
1,2024-01-03 10:00,2024-01-03 11:15,182.5,184.2,1.7,2.1
2,2024-01-03 13:40,2024-01-03 14:10,183.8,183.1,-0.7,-1.0

🧭 2. Exports JSON

2.1 Résumé de Performance

json
{
  "total_return_pct": 12.4,
  "max_drawdown_pct": -6.8,
  "sharpe_ratio": 1.42,
  "win_rate_pct": 54.3,
  "number_of_trades": 87
}
2.2 Configuration d’Optimisation
json
{
  "ema_length": 114,
  "rsi_length": 14,
  "volume_threshold": 1.5,
  "stop_loss_pct": 1.5,
  "take_profit_pct": 3.0,
  "min_score_threshold": 70
}

🧭 3. Exports Markdown

3.1 Rapport de Backtest

markdown
# 📈 Rapport de Backtest — Stratégie EMA 114

- **Rendement total** : 12.4%
- **Drawdown max** : -6.8%
- **Sharpe ratio** : 1.42
- **Trades gagnants** : 54.3%
- **Nombre de trades** : 87

## 📊 Courbe d’Équité
*(voir equity_curve.png)*

## 🧠 Analyse IA
- Score moyen : 68.2
- Score max : 92

🧭 4. Exports Visuels

4.1 Courbe d’Équité

Code
exports/visuals/equity_curve.png

4.2 Heatmap de Prédictibilité

Code
exports/visuals/predictability_heatmap.png
