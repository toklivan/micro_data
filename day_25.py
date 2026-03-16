# Day 25
# Carte : Nettoyage simple

raw_products = [
    " apple ",
    "banana",
    "APPLE",
    " banana ",
    "orange",
    "Orange ",
    " banana"
]

# 1 Create a new 'clean_products' list.

# 2 Course 'raw_products'.

# 3 For each product: remove spaces with 'strip()'.
#                     convert the text to lowercase with 'lower()'.

# 4 Add the cleaned product in 'clean_products'.

# 5 Display 'clean_products'.

# 6 Then create a 'unique_products' list.

# 7 Parcours 'clean_products' and adds only the products not already present
#   in 'unique_products'.

# 8 Display 'unique_products'.

clean_products: list[str] = []

for product in raw_products:
    clean_products.append(product.strip().lower())
print(clean_products)

unique_products: list[str] = []

for product in clean_products:
    if product not in unique_products:
        unique_products.append(product)
print(unique_products)

# Business question.

print("\n=== Business answer ===\n")
print("Cleaning and standardizing product names is essential to avoid the")
print("same product appearing under several different names,")
print("which would distort the analysis of sales.")
