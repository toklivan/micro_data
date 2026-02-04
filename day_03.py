# Day 03
# Carte : CSV

data = [
    "lundi,120",
    "mardi,95",
    "mercredi,110",
    "jeudi,0",
    "vendredi,160"
    ]

# 1 Transforms each line into day and sale (separation by ,).

for line in data:
    parts = line.split(",")
    print(parts)

# 2 Stock this data in a 'sales' dictionary.

sales = {}

for line in data:
    parts = line.split(",")
    sales[parts[0]] = int(parts[1])

print(sales)

# 3 Calculate the total sales.

total = 0
for value in sales.values():
    total += value

print(f"Total sales = {total}")

# 4 Calculate the average of sales.

average = total / len(sales)
print(f"Average sales = {average}")

# 5 Display the day with the highest sale.

high = max(sales, key=sales.get)
print(f"The highest sale is {high} with {sales[high]}")

# 6 Display the day with the lowest sale.

low = min(sales, key=sales.get)
print(f"The lowest sale is {low} with {sales[low]}")

# Business analysis

print("The key information to recover is the weakest day of the week.")
print("Because we can act immediately to correct")
