# Day 32
# Carte : Dictionnaire

orders = [
    {"product": "apple", "quantity": 3},
    {"product": "banana", "quantity": 2},
    {"product": "apple", "quantity": 4},
    {"product": "orange", "quantity": 1},
    {"product": "banana", "quantity": 5}
]

# 1 Create a sales_by_product dictionary.

# 2 Browse the orders list.

# 3 For each order: - recover product.
#                   - recover quantity.

# 4 Add the quantities by product in the dictionary.

# 5 Diaplay sales_by_product.

# 6 Calculate the total sales (all qunatities).

# 7 Display this total.

# 8 Calculate the share (%) of each product.

# 9 Display each product with its percentage.

# 10 Find the product with the smallest part (without using min()).

# 11 Display this protuct.

sales_by_product: dict = {}

for order in orders:
    product = order["product"]
    quantity = order["quantity"]
    sales_by_product[product] = sales_by_product.get(product, 0) + quantity
print(sales_by_product)

total_sales = 0
for values in sales_by_product.values():
    total_sales += values
print(f"The total of sales is {total_sales}")

min_product = None
min_value = None

for product, quantity in sales_by_product.items():
    percentage = (quantity * 100) / total_sales
    print(f"{product}: {percentage:.0f}%")

    if min_value is None or percentage < min_value:
        min_product = product
        min_value = percentage
print(f"The smallest part product is {min_product} with {min_value:.0f}%")

# Business question

print("\n=== Business answer ===\n")
print("Identifying the product that contributes the")
print("least to sales is important because it allows")
print("correcting or removing what does not bring")
print("value and optimizing profitability.")
print("\n=== Business answer ===\n")
