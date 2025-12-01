# EXERCICE 2 - CORRECTION D'ERREURS
# Corrigez toutes les erreurs dans ce code

# Données de l'inventaire
produits = ["pommes", "bananes", "oranges", "kiwis"]
stocks = [15, 8, 12, 5]
prix = [1.2, 0.8, 1.5, 2.0]

# 1. Affichage de l'inventaire
print("=== INVENTAIRE ===")
for i in range(len(produits)):
    print(f"{produits[i]} - Stock: {stocks[i]} - Prix: {prix[i]}$")

# 2. Calcul du stock total
stock_total = sum(stocks)
print(f"\nStock total: {stock_total}")

# 3. Produit le plus cher
index_plus_cher = prix.index(max(prix))
produit_plus_cher = produits[index_plus_cher]
print(f"Produit le plus cher: {produit_plus_cher}")

# 4. Produits en rupture de stock
ruptures = []
for i in range(len(stocks)):
    if stocks[i] == 0:
        ruptures.append(produits[i])

print(f"Produits en rupture: {ruptures}")

# 5. Ajout d'un nouveau produit
nouveau_produit = "mangues"
nouveau_stock = 10
nouveau_prix = 1.8

produits.append(nouveau_produit)
stocks = stocks.append(nouveau_stock)
prix.append(nouveau_prix)

print(f"\nAprès ajout de {nouveau_produit}:")
print(f"Produits: {produits}")
print(f"Stocks: {stocks}")
print(f"Prix: {prix}")

# 6. Vérification des types
print(f"\nTypes des données:")
print(f"Type de produits: {type(produits)}")
print(f"Type de stocks: {type(stocks)}")
print(f"Type de prix: {type(prix)}")