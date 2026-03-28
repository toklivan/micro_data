# Day 30
# Carte : CSV

rows = [
    "produit,quantite",
    "apple,3",
    "banana,2",
    "apple,4",
    "orange,1",
    "banana,5",
    "apple,2"
]

# 1 Create a 'sales_by_product' dictionary.

# 2 Ignore the header.

# 3 Course the remaining lines.

# 4 For each line: - use 'split(",")'.
#                  - recovers product and quantity.

# 5 Converts quantities in int.

# 6 Adds quantities by product in the dictionary.

# 7 Display 'sales_by_product'.

# 8 Calculate the percentage of each product in relation to total sales.

# 9 Display each product with is percentage (e.g. apple: 45%).

# 10 Identify the product that represents the largest share (without max()).

# 11 Display this product.

sales_by_product: dict[str, int] = {}

for line in rows[1:]:
    parts = line.split(",")
    product = parts[0]
    quantity = int(parts[1])
    sales_by_product[product] = sales_by_product.get(product, 0) + quantity
print(sales_by_product)

total_sales: int = sum(sales_by_product.values())

for product, quantity in sales_by_product.items():
    percentage = (quantity * 100) / total_sales
    print(f"{product}: {percentage:.0f}%")

max_product = None
max_value = None

for product in sales_by_product:
    if max_value is None or sales_by_product[product] > max_value:
        max_product = product
        max_value = sales_by_product[product]
print(f"The largest share product is {max_product}")

# Business question

print("\n=== Business answer ===\n")
print("Knowing the share (%) of each product is more")
print("useful because it shows the real weight of each")
print("product in sales and allows for better")
print("prioritizing decisions.")
