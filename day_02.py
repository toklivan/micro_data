# Day 02
# Carte : Dictionnaire

sales = {
    "lundi": 120,
    "mardi": 95,
    "mercredi": 110,
    "jeudi": 0,
    "vendredi": 160
}

# 1 Display all the keys of the dictionary.

for key in sales:
    print(key)

# 2 Display all values of the dictionary.

for value in sales:
    print(sales[value])

# 3 Calculate the total sales for the week.

total = 0
for value in sales.values():
    total += value
print(f"Total sales = {total}")

# 4 Calculate the average of sales.

average = total / len(sales.values())
print(f"Average sales = {average}")

# 5 Display the day with the highest sale.

high = max(sales, key=sales.get)
print(f"The highest sale is {high} with {sales[high]}")

# 6 Dsiplay the day with the lowest sale.

low = min(sales, key=sales.get)
print(f"The lowest sale  is {low} with {sales[low]}")

# Business analysis.
print("Friday contributes the most to the revenue.")
print("Thursday is a problem because there are no sales.")
