import pandas as pd
from multi_tf_contextualizer import add_timeframe_context

df = pd.DataFrame([
    {"timestamp":"2025-12-16 09:00:00","open":100,"high":105,"low":95,"close":102},
    {"timestamp":"2025-12-16 09:15:00","open":102,"high":108,"low":100,"close":107},
    {"timestamp":"2025-12-16 09:30:00","open":107,"high":110,"low":105,"close":109},
    {"timestamp":"2025-12-16 10:00:00","open":109,"high":111,"low":108,"close":110},
])

print(add_timeframe_context(df,"1H"))
