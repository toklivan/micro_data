# Day 20
# Carte : CSV

rows = [
    "apple,3",
    "banana,2",
    "apple,4",
    "orange,1",
    "banana,5"
]

# 1 For each line, separate the product and quantity with 'split(",")'.

# 2 Store this data in a 'sales_by_product' dictionary.

# 3 If a product appears several times, add the quantity instead of
# overwriting the old quantity.

sales_by_product: dict[str, int] = {}

for line in rows:
    parts = line.split(",")
    product = parts[0]
    quantity = int(parts[1])
    if product not in sales_by_product:
        sales_by_product[product] = quantity
    else:
        sales_by_product[product] += quantity

# 4 Displays the final 'sales_by_product' dictionary.

print(sales_by_product)

# 5 Calculate the total sales.

total: int = 0

for product in sales_by_product:
    total += sales_by_product[product]
print(f"The total of sales is {total}")

# 6 Displays the best-selling product (name + quantity).

best_product = None
best_quantity = None

for product in sales_by_product:
    quantity = sales_by_product[product]

    if best_quantity is None or quantity > best_quantity:
        best_quantity = quantity
        best_product = product

print(f"The best-selling product is {best_product} with {best_quantity}")

# Business decision.

print("\n=== Business Analysis ===\n")
print("Because grouping the lines of a same product allows to know its real")
print("total sales, otherwise one risks underestimating a product and making")
print("a bad decision on what to highlight.")
