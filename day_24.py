# Day 24
# Carte : Dictionnaire

product_prices = {
    "apple": 1.2,
    "banana": 0.8,
    "orange": 1.5,
    "mango": 2.0,
    "grape": 1.8
}

# 1 Create a variable 'total_price' and calculate the sum of all prices with
#   a loop.

# 2 Calculates the average price of the products.

# 3 Displays the average price.

# 4 Find the cheapest product without using 'min()'.

# 5 Displays the name of the cheapest product and its price.

# 6 Count how many products have a price above the average price.

# 7 Print this number.

total_price: float = 0.0

for price in product_prices.values():
    total_price += price

average_price: float = total_price / len(product_prices)

print(f"The average price is {average_price}")

cheapest_product = None
cheapest_price = None

for product, price in product_prices.items():
    if cheapest_price is None or price < cheapest_price:
        cheapest_price = price
        cheapest_product = product

print(f"The cheapest product is {cheapest_product} at {cheapest_price} euros")

product_above: int = 0
for price in product_prices.values():
    if price > average_price:
        product_above += 1

print(f"The number of product are above average is {product_above}")

# Business question.

print("\n=== Business answer ===\n")
print("Identifying products above the average price allows you to identify")
print("those that are the most expensive and decide whether to adjust their")
print("price or justify their positioning.")
