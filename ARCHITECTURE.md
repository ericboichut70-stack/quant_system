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
