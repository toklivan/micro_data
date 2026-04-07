# Day 34
# Carte : Réécriture / simplification

clean_orders = [
    {"product": "apple", "quantity": 3},
    {"product": "banana", "quantity": 2},
    {"product": "apple", "quantity": 4},
    {"product": "orange", "quantity": 1},
    {"product": "banana", "quantity": 5}
]

# sales_by_product = {}

# for order in clean_orders:
#     product = order["product"]
#     quantity = order["quantity"]

#     if product not in sales_by_product:
#         sales_by_product[product] = quantity
#     else:
#         sales_by_product[product] += quantity

# print(sales_by_product)

# 1 Rewrite the loop to use get() instead of if/else.

# 2 Checks that the result is identical.

# 3 Add a loop to display each product with its quantity.

# 4 Creates a variable total_sales and calculates the total quantities.

# 5 Display the total.

# 6 Calculate the percentage of each product.

# 7 Display each product with its percentage (e.g. apple: 46%).

sales_by_product: dict = {}

for order in clean_orders:
    product = order["product"]
    quantity = order["quantity"]

    sales_by_product[product] = sales_by_product.get(product, 0) + quantity

print(sales_by_product)

for key, value in sales_by_product.items():
    print(f"{key}: {value}")

total_sales = 0
for value in sales_by_product.values():
    total_sales += value
print(f"The total quantities is {total_sales}")

for product, quantity in sales_by_product.items():
    percentage = (quantity * 100) / total_sales
    print(f"{product}: {percentage:.0f}%")

# Business question

print("\n=== Business answer ===\n")
print("Simplifying the code is essential because it")
print("allows several people to understand it quickly,")
print("modify it without error and ensure reliable")
print("analyses in a team.")
