# Day 16
# Carte : Liste

basket_values: list[int] = [12, 7, 15, 3, 20, 9, 11]

# 1 Displays all the values of the basket.

print("=== The values of the basket ===")
for values in basket_values:
    print(values)

# 2 Calculate the total of the baskets.

total: int = 0
for values in basket_values:
    total += values
print("The total of the baskets is : ", total)

# 3 Calculate the average of the baskets.

average: float = total / len(basket_values)
print("The average of the baskets is : ", average)

# 4 Find the maximum value (without max()).

max_value = basket_values[0]
for values in basket_values:
    if values > max_value:
        max_value = values
print("The maximum value is : ", max_value)

# 5 Find the minumum value (without min()).

min_value = basket_values[0]
for values in basket_values:
    if values < min_value:
        min_value = values
print("The minimum value is : ", min_value)

print("\n=== Business Analysis ===\n")
print("If these amounts are average baskets, \
I can set up a complementary offer or promotion to encourage customers \
to add a product and increase the average.")
