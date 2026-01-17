# === Définition d'une fonction d'objectif ===
import optuna

def objective(trial):
    ema = trial.suggest_int("ema", 10, 200)
    rsi = trial.suggest_int("rsi", 10, 30)
    volume_thresh = trial.suggest_float("volume_ratio", 1.0, 3.0)
    sl = trial.suggest_float("sl_pct", 0.5, 3.0)
    tp = trial.suggest_float("tp_pct", 1.0, 5.0)

    df_optuna = yf.download("AAPL", start="2020-01-01", end="2023-01-01")
    df_optuna = df_optuna.rename(columns={'Open': 'open', 'High': 'high', 'Low': 'low', 'Close': 'close', 'Volume': 'volume'})

    indicator = IndicatorModule(ema, rsi, volume_thresh)
    df_ind = indicator.compute_indicators(df_optuna)
    df_sig = indicator.compute_signals(df_ind)
    df_trd = indicator.compute_trade_management(df_sig, trail_pct=1.0, sl_pct=sl, tp_pct=tp)
    df_eval = indicator.evaluate_performance(df_trd)

    score = (
        (df_eval['TradeResult'] == 'TP Hit').sum() * 2
        - (df_eval['TradeResult'] == 'SL Hit').sum()
        + df_eval['ScoreIA'].mean() * 0.1
    )
    return score

# Optimisation
study = optuna.create_study(direction="maximize")
study.optimize(objective, n_trials=50)
print(study.best_params)