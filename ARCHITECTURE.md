# Diagramme logique en ASCII, transformable en schéma visuel plus tard

               +------------------+
                |  data_loader.py  |
                +---------+--------+
                          |
                          v
             +---------------------------+
             |   df prix de marché       |
             | (timestamp, O/H/L/C, vol) |
             +---------------------------+
         /            |             \
        v             v              v
+---------------+  +-----------------+  +----------------------+
| trend_detector|  |volatility_clust.|  |  orderflow_reader    |
+-------+-------+  +--------+--------+  +----------+-----------+
        |                   |                     |
        v                   v                     v
  +-----------+      +------------+        +--------------+
  |  Trend    |      | Volatility |        | Orderflow    |
  +-----------+      +------------+        +--------------+

        +-----------------------------------------------+
        |        structure_tracker & zigzag_mapper      |
        +--------------------+--------------------------+
                             |
                             v
                         +--------+
                         |Struct. |
                         +--------+

        +-----------------------------------------------+
        |  sentiment_analyzer & signal_predictor        |
        +--------------------+--------------------------+
                             |
                             v
                         +--------+
                         |Signals |
                         +--------+

        +-------------------------------+
        | signal_attribution & optimizer|
        +------------------+------------+
                           |
                           v
                     +-----------+
                     | Final Sig |
                     +-----------+

                           |
                           v
              +--------------------------+
              | signature_generator.py   |
              +-------------+------------+
                            |
                            v
                     +-------------+
                     | trading_api |
                     +-------------+

A lire comme : données → analyse → structure & flux → signaux → attribution & optimisation → signature → exécution.

---

## ✅ Diagramme d’architecture (textuel)

quant_system/
│
├── data/
│
├── loader.py│
└── preprocess.py│
├── indicators/│
├── ema.py
│
├── adx.py│
└── volatility.py│
├── structure/│
├── swings.py│
└── zigzag.py │
├── orderflow/│
├── delta.py│
├── imbalance.py│
└── absorption.py│
├── features/│
├── feature_builder.py│
└── encoders.py│
├── signals/│
├── signal_engine.py│
└── scoring.py│
├── optimization/│
└── parameter_search.py │
── attribution/│
└── attribution_engine.py│
├── utils/│
├── hashing.py│
└── helpers.py│
└── pipeline/
└── run_pipeline.py
