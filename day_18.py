# Day 18
# Carte : CSV

rows = [
    "product_A,42",
    "product_B,30",
    "product_C,55",
    "product_D,18",
    "product_E,25"
]

# 1 For each line, separate the product and quantity with 'split(",").

for line in rows:
    parts = line.split(",")

# 2 Store data in a dictionary 'sales_by_product'.

sales_by_product: dict[str, int] = {}

for line in rows:
    parts = line.split(",")
    key = parts[0]
    value = int(parts[1])
    sales_by_product[key] = value
print(sales_by_product)

# 3 Calculate the total sales.

total: int = 0
for value in sales_by_product.values():
    total += value
print(f"The total sales is {total}")

# 4 Calculate the average of sales.

average: float = total / len(sales_by_product)
print(f"The average of sales is {average}")

# 5 Find the least-selling product (name + quantity).

max_key = None
max_sale = None
for key in sales_by_product:
    if max_sale is None or sales_by_product[key] > max_sale:
        max_sale = sales_by_product[key]
        max_key = key
print(f"The least-selling product is {max_key} with {max_sale}")

# 6 Find the least sold product (name + quantity).

least_key = None
least_sale = None
for key in sales_by_product:
    if least_sale is None or sales_by_product[key] < least_sale:
        least_sale = sales_by_product[key]
        least_key = key
print(f"The least-selling product is {least_key} with {least_sale}")

# Business analysis.

print("\n=== Business Analysis ===\n")
print("The product that needs to be prioritized in order to maximize sales is\
 product_C, because it is the best-selling product.")
