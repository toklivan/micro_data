# Day 22
# Carte : CSV

rows = [
    "produit,quantite",
    "apple,3",
    "banana,2",
    "apple,4",
    "orange,1",
    "banana,5"
]

# 1 Creates a blank dictionary to store the total quantities per product.
# 2 Ignore first line, because its the header.
# 3 Browse the other lines one by one.
# 4 Cut each line with 'split(",")' to retrieve: the product name,
#                                                the quantity.
# 5 Convert the quantity to full.
# 6 Add the quantities in a dictionary.
# 7 Displays the final dictionary.
# 8 Then displays the best-selling product and quantity, whitout using 'max()'.

sales_by_product: dict[str, int] = {}

for line in rows[1:]:
    parts = line.split(",")
    product = parts[0]
    quantity = int(parts[1])
    if product not in sales_by_product:
        sales_by_product[product] = quantity
    else:
        sales_by_product[product] += quantity
print(sales_by_product)

best_product = None
best_quantity = None

for product, quantity in sales_by_product.items():
    if best_quantity is None or quantity > best_quantity:
        best_quantity = quantity
        best_product = product
print(f"The best-selling product is {best_product} with {best_quantity}")

# Business question.

print("\n=== Business answer ===\n")
print("Because grouping the sales of the same product allows to know its real")
print("total volume, otherwise one can underestimate a product and make a bad")
print("decision on which to highlight.")
