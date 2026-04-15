# Day 40
# Carte : Réécriture / simplification

orders = [
    {"customer": "Alice", "product": "apple", "amount": 12.0},
    {"customer": "Bob", "product": "banana", "amount": 8.0},
    {"customer": "Alice", "product": "orange", "amount": 5.0},
    {"customer": "Bob", "product": "apple", "amount": 7.0},
    {"customer": "Charlie", "product": "banana", "amount": 10.0},
    {"customer": "Alice", "product": "banana", "amount": 6.0}
]

# 1 Create a revenue_by_customer dictionary.

# 2 Path orders and calculates the total spent per customer (use get()).

# 3 Displays revenue_by_customer.

# 4 Create a revenue_by_product dictionary.

# 5 Path orders and calculates the total generated per product (use get()).

# 6 Displays revenue_by_product.

# 7 Calculates total revenue (all orders).

# 8 Show this total.

# 9 Find : - the best client (largest amount).
#          - the best product (highest revenue).
#   whitout using max().

# 10 Displays these two results.

revenue_by_customer: dict = {}

for order in orders:
    customer = order["customer"]
    amount = order["amount"]
    revenue_by_customer[customer] = revenue_by_customer.get(customer, 0.0) + amount

print(revenue_by_customer)

revenue_by_product: dict = {}

for order in orders:
    product = order["product"]
    amount = order["amount"]
    revenue_by_product[product] = revenue_by_product.get(product, 0.0) + amount

print(revenue_by_product)

total_revenue = 0.0

for order in orders:
    amount = order["amount"]
    total_revenue += amount

print(f"The total revenue is {total_revenue}")

max_customer = None
max_product = None
max_amount = None
for client, value in revenue_by_customer.items():
    if max_amount is None or value > max_amount:
        max_amount = value
        max_customer = customer

print(f"The best client is {max_customer} with {max_amount}")

max_amount = None
for product, value in revenue_by_product.items():
    if max_amount is None or value > max_amount:
        max_amount = value
        max_product = product

print(f"The best product is {max_product} with {max_amount}")

# Business question.

print("\n=== Business answer ===\n")
print("Cross-analyzing by customer and by product is")
print("essential because it allows us to understand who")
print("buys what and to adapt actions to maximize sales.")
