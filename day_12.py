# Day 12
# Carte : Dictionnaire

sales_by_product = {
    "apple": 42,
    "banana": 30,
    "orange": 55,
    "pear": 18,
    "kiwi": 25
}

# 1 Display all products.

for products in sales_by_product.keys():
    print(products)

# 2 Displays all quantities sold.

for nb_sales in sales_by_product.values():
    print(nb_sales)

# 3 Calculate the total sales.

total_sales: int = 0
for nb_sales in sales_by_product.values():
    total_sales += nb_sales
print(f"The total sales is : {total_sales}")

# 4 Calculate the average of sales by product.

length: int = 0
for _ in sales_by_product.values():
    length += 1
average: float = total_sales / length
print(f"The average of sales is : {average}")

# 5 Displays the best-selling product (name + quantity).

max_product = None
max_sales = None
for products in sales_by_product:
    sales: int = sales_by_product[products]
    if max_sales is None or sales > max_sales:
        max_sales = sales
        max_product = products
print(f"The best-selling product is {max_product} with {max_sales}")

# 6 Displays the product with the lowest sales (name + quantity).

min_product = None
min_sales = None
for products in sales_by_product:
    sales_amount: int = sales_by_product[products]
    if min_sales is None or sales_amount < min_sales:
        min_sales = sales_amount
        min_product = products
print(f"The product with the lowest sales is {min_product} with {min_sales}")

# Business analysis.

print("\n=== Business Decision ===\n")
print("Product to highlight = orange (55 sales)")