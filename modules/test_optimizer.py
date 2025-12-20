import pandas as pd
from optimizer import optimize_parameters, apply_optimized_parameters, summarize_optimization

df = pd.DataFrame([
    {"close":100},
    {"close":102},
    {"close":101},
    {"close":105},
    {"close":103},
    {"close":110},
])

params = optimize_parameters(df)
print("Paramètres optimisés :", params)

optimized = apply_optimized_parameters(df, params)
print("\nDataFrame enrichi :")
print(optimized)

print("\nRésumé :")
print(summarize_optimization(optimized))
