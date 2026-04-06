# Day 33
# Carte : Nettoyage simple

raw_orders = [
    {"product": " apple ", "quantity": "3"},
    {"product": "BANANA", "quantity": "2"},
    {"product": "apple", "quantity": "4"},
    {"product": " Orange ", "quantity": "1"},
    {"product": "banana ", "quantity": "5"}
]

# 1 Create a new clean_orders list.

# 2 Parcours raw_orders.

# 3 For each element: - clean product with strip() ans lower().
#                     - convert quantity to int.

# 4 Create a new dictionary of your own with: {"product": ..., "quantity": ...}

# 5 Add this dictionary in clean_orders.

# 6 Display clean_orders.

# 7 Create a sales_by_product dictionary.

# 8 Parcours clean_orders and adds the quantities by product.

# 9 Display sales_by_product.

clean_orders: list[dict[str, int]] = []

for order in raw_orders:
    clean_orders.append({
        "product": order["product"].strip().lower(),
        "quantity": int(order["quantity"])
    })

print("clean_orders:", clean_orders)

sales_by_product: dict[str, int] = {}

for order in clean_orders:
    product = order["product"]
    sales_by_product[product] = sales_by_product.get(product, 0) + order["quantity"]

print("sales_by_product:", sales_by_product)

# Business question

print("\n=== Business answer ===\n")
print("Cleaning the data before aggregation ensures that")
print("each entity is uniquely identified, otherwise")
print("inconsistencies (spaces, case, types) skew totals")
print("and lead to poor decisions.")
