# Day 05
# Carte : Reecriture / simplification

# Code original.
sales = {
    "lundi": 120,
    "mardi": 95,
    "mercredi": 110,
    "jeudi": 0,
    "vendredi": 160
}

total = 0
for key in sales:
    total = total + sales[key]

average = total / len(sales)

best_day = None
best_value = 0
for day in sales:
    if sales[day] > best_value:
        best_value = sales[day]
        best_day = day

print("Total:", total)
print("Average:", average)
print("best day:", best_day, best_value)

# Code simplifie.
total = 0
for value in sales.values():
    total += value

average = total / len(sales)

best_day = max(sales, key=sales.get)

print(f"Total: {total}\nAverage: {average}\nBest day: {best_day} {sales[best_day]}")

# Business analysis.
print("\n=== Business analysis ===\n")
print("If the code is not readable, people do not trust calculations.")
print("So they do not trust the decisions.")
