# Day 38
# Carte : Dictionnaire

orders = [
    {"product": "apple", "price": 1.2, "quantity": 3},
    {"product": "banana", "price": 0.8, "quantity": 2},
    {"product": "apple", "price": 1.2, "quantity": 4},
    {"product": "orange", "price": 1.5, "quantity": 1},
    {"product": "banana", "price": 0.8, "quantity": 5}
]

# 1 Creates a revenue_by_product dictionary.

# 2 Browse the orders list.

# 3 For each order : - retrieves product, price, quantity.

# 4 Calculates the revenue for each line (price * quantity).

# 5 Adds the revenue per product.

# 6 Diaplay revenue_by_product.

# 7 Find the product with the lowest revenue (without using min()).

# 8 Displays this product and its amount.

revenue_by_product: dict = {}

for order in orders:
    product = order["product"]
    price = order["price"]
    quantity = order["quantity"]
    revenue = price * quantity
    revenue_by_product[product] = revenue_by_product.get(product, 0) + revenue

print(revenue_by_product)

min_revenue = None
min_product = None

for product, revenue in revenue_by_product.items():
    if min_revenue is None or revenue < min_revenue:
        min_revenue = revenue
        min_product = product

print(f"The product with the lowest revenue is "
      f"{min_product} with {min_revenue}")
