# Day 27
# Carte : Reecriture / simplification

clean_products = [
    "apple",
    "banana",
    "apple",
    "orange",
    "banana",
    "apple",
    "banana"
]

# product_counts = {}

# for product in clean_products:
#     if product not in product_counts:
#         product_counts[product] = 1
#     else:
#         product_counts[product] += 1

# print(product_counts)

# 1 Rewrite the counting loop using 'get()' to remove the if / else.

# 2 Checks that the result is identical.

# 3 Adds a loop to display each product with its quantity in the form:
#   - apple: 3
#   - banana: 3
#   - orange: 1

# 4 Adds a variable total_products and calculates the total of products sold
#   (sum of quantities).

# 5 Display this total.

product_counts: dict[str, int] = {}

for product in clean_products:
    product_counts[product] = product_counts.get(product, 0) + 1
print(product_counts)

for product, value in product_counts.items():
    print(f"{product}: {value}")

total_products = 0
for value in product_counts.values():
    total_products += value
print(f"The total of product sold is {total_products}")

# Business question

print("\n=== Business answer ===\n")
print("Simplifying the code is important because it reduces errors and allows")
print("the whole team to understand and correctly use the data to make")
print("reliable decisions.")
