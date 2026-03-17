# Day 26
# Carte : Dictionnaire

clean_products = [
    "apple",
    "banana",
    "apple",
    "orange",
    "banana",
    "apple",
    "banana"
]

# 1 Create an empty 'product_counts' dictionary.

# 2 Browse the 'clean_product' list.

# 3 For each product : - if it is not in the dictionary initializes to 1.
#                      - otherwise increment of 1.

# 4 Displays the final dictionary.

# 5 Find the most common product without using max().

# 6 Displays this product and its number of occurences.

product_counts: dict[str, int] = {}

for product in clean_products:
    if product not in product_counts:
        product_counts[product] = 1
    else:
        product_counts[product] += 1
print(product_counts)

max_product = None
max_value = None

for product in product_counts:
    if max_value is None or product_counts[product] > max_value:
        max_product = product
        max_value = product_counts[product]
print(f"The most common product is {max_product} with {max_value}")

# Business question.

print("\n=== Business answer ===\n")
print("Knowing the best-selling product is essential because it allows")
print("focusing efforts on what generates the most sales and optimizing")
print("business decisions.")
