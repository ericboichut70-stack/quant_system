# 📘 `docs/architecture/diagrams/module_dependencies.md`

```markdown
# 🧬 Module Dependencies — Dépendances des Modules

Ce diagramme montre les dépendances internes entre les modules quantitatifs.

```mermaid
flowchart LR

    A[Indicators] --> B[Structure Module]
    A --> C[Volatility Module]
    A --> D[Orderflow Module]

    B --> E[Signal Filter]
    C --> E
    D --> E

    E --> F[Strategy]
