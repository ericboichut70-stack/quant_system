# Manifest technique du TRADING_BOT

## 1. Données d’entrée standard

Sauf mention contraire, les modules manipulent des `pandas.DataFrame` avec les colonnes suivantes :

- Prix : `timestamp`, `open`, `high`, `low`, `close`, `volume`
- Volumes directionnels : `buy_volume`, `sell_volume`
- Signaux : `Signal`, `Trend`, `Sentiment`, `ConvergentSignal`, `PredictedSignal`
- Métriques dérivées : `Return`, `Volatility`, `VolumeNorm`, `EMA`, `Momentum`, `Slope`, `ADX`
- Structure : `SwingHigh`, `SwingLow`, `Structure`
- ZigZag : `Pivot`, `PivotType`
- Orderflow : `Delta`, `Imbalance`, `Absorption`
- Optimisation : `Energy`, `Filtered`
- Traçabilité : `Signature`

## 2. Chaîne de traitement recommandée

1. **Préparation des données**
   - Module(s) : `data_loader.py` (ou équivalent maison)
   - Sortie : DataFrame de base avec `timestamp, open, high, low, close, volume`.

2. **Analyse de tendance et de régime**
   - `trend_detector.detect_trend(df)` → ajoute `Slope`, `ADX`, `Trend`, `TrendCode`.
   - `volatility_clustering.detect_volatility_clusters(df)` → ajoute `Volatility`, `Cluster`.

3. **Structure de marché & ZigZag**
   - `structure_tracker.detect_market_structure(df)` → `SwingHigh`, `SwingLow`, `Structure`.
   - `zigzag_mapper.compute_zigzag(df)` → `Pivot`, `PivotType`.

4. **Orderflow & sentiment**
   - `orderflow_reader.compute_orderflow(df)` → `Delta`, `Imbalance`, `Absorption`.
   - `sentiment_analyzer.analyze_sentiment(df)` → `Variation`, `Sentiment`.

5. **Prédiction & optimisation**
   - `signal_predictor.extract_features` + `enrich_features` + `predict_signals` → `PredictedSignal`.
   - `optimizer.optimize_parameters` + `apply_optimized_parameters` → `ConvergentSignal`.

6. **Attribution & traçabilité**
   - `signal_attribution.attribute_signals(df)` → `Attribution`.
   - `signature_generator.add_signatures(df)` → `Signature`.

7. **Exécution simulée**
   - `trading_api.place_order`, `fetch_positions`, `close_position`.

## 3. Conventions de codage

- Aucun code exécuté au niveau module : uniquement des définitions de fonctions.
- Pas d’imports circulaires entre modules.
- Tous les modules disposent :
  - d’une fonction principale de transformation,
  - d’une fonction de résumé human‑readable (`summarize_*`), quand c’est pertinent.
- Les scripts de test sont séparés (`test_*.py`) et ne polluent pas les modules.

✅ ## Version datée — Stabilisation du code

Version stabilisée du TRADING_BOT  
Date : 20 décembre 2025 — 12:05 CET  
Statut : ✅ Conforme, ✅ Testée, ✅ Auditée, ✅ Documentée

Cette version constitue la base de référence pour les développements futurs.
