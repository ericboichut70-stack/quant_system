from trading_api import place_order, fetch_positions, close_position

# --- Test placement d'ordre ---
order = place_order("BTCUSD", "Buy", 0.3, 41000)
print("Ordre placé :")
print(order)

# --- Test récupération des positions ---
positions = fetch_positions()
print("\nPositions ouvertes :")
print(positions)

# --- Test fermeture d'une position ---
closed = close_position("BTCUSD")
print("\nPosition fermée :")
print(closed)
