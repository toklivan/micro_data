# Day 28
# Carte : CSV

rows = [
    "produit,prix,quantite",
    "apple,1.2,3",
    "banana,0.8,2",
    "apple,1.2,4",
    "orange,1.5,1",
    "banana,0.8,5"
]

# 1 Create a dictionary 'revenue_by_product'.

# 2 Ignore the first line (header).

# 3 Browse the remaining lines.

# 4 For each line: - use 'split(",")'.
#                  - retrieve product, price, quantity.

# 5 Converts: - price in float.
#             - quantity in int.

# 6 Calculates the line's turnover (price * quantity).

# 7 Add this amount in the dictionary (aggregation by product).

# 8 Display 'revenue_by_product'.

# 9 Calculates the total turnover.

# 10 Displays the total.

revenue_by_product: dict[str, float] = {}

for line in rows[1:]:
    parts = line.split(",")
    product = parts[0]
    price = float(parts[1])
    quantity = int(parts[2])
    turnover = price * quantity
    if product not in revenue_by_product:
        revenue_by_product[product] = turnover
    else:
        revenue_by_product[product] += turnover

print(revenue_by_product)

total_turnover = 0.0
for turnover in revenue_by_product.values():
    total_turnover += turnover
print(f"The total turnover is {total_turnover:.1f}")

# Business question

print("\n=== Business answer ===\n")
print("Analysing the turnover by product is more relevant because it show")
print("the real value generated, while quantities alone do not reflect")
print("the financial impact.")
