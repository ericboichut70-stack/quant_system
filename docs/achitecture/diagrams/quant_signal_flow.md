# 📘 `docs/architecture/diagrams/quant_signal_flow.md`

```markdown
# 🔄 Quant Signal Flow — Flux des Signaux Quantitatifs

Ce diagramme montre comment les signaux circulent dans le moteur quantitatif.

```mermaid
sequenceDiagram
    participant D as Data
    participant I as Indicators
    participant Q as Quant Modules
    participant S as Strategy
    participant B as Backtest
    participant E as Exports

    D->>I: Données normalisées
    I->>Q: Features enrichies
    Q->>S: Signaux avancés
    S->>B: Ordres & règles
    B->>E: Résultats & métriques
