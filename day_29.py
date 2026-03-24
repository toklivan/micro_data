# Day 29
# Carte : Nettoyage simple

raw_prices = [
    " 1.2",
    "0.8 ",
    " 1.5 ",
    "2.0",
    " 0.9"
]

# 1 Create a new 'clean_price' list.

# 2 Courses 'raw_prices'.

# 3 For each element: - removes spaces with 'strip()'.
#                     - convert the value into a float.

# 4 Adds the cleaned value in 'clean_prices'.

# 5 Display 'clean_prices'.

# 6 Create a variable 'total_price' and calculate the sum of price with a loop.

# 7 Calculate the average price.

# 8 Displays the average price.

# 9 Find the highest price without using 'max()'.

# 10 Diplay this price.

clean_prices: list[float] = []

for line in raw_prices:
    prices = float(line.strip())
    clean_prices.append(prices)

print(clean_prices)

total_price = 0.0
for price in clean_prices:
    total_price += price
average_price = total_price / len(clean_prices)
print(f"The average price is {average_price}")

highest_price = None
for price in clean_prices:
    if highest_price is None or highest_price < price:
        highest_price = price
print(f"The highest price is {highest_price}")

# Business question.

print("\n=== Business answer ===\n")
print("Cleaning prices before calculation is essential")
print("because incorrect or inconsistent formats can")
print("distort the results and lead to poor decisions.")
