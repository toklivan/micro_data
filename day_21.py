# Day 21
# Carte : Liste

daily_customers = [45, 52, 38, 60, 41, 55, 47]

# 1 Displays all customer numbers.

for number in daily_customers:
    print(number)

# 2 Calculate the total number of customers for the week.

total: int = 0
for number in daily_customers:
    total += number
print(f"The total number of customers for the week is {total}")

# 3 Calculate the average number of customers per day.

average: float = total / len(daily_customers)
print(f"The average number of customers is {average:.2f}")

# 4 Find the day with the most customers (number only).
# 5 Find the day with the fewest customers.

most_customers = None
fewest_customers = None

for number in daily_customers:
    if most_customers is None or number > most_customers:
        most_customers = number
    if fewest_customers is None or number < fewest_customers:
        fewest_customers = number

print(f"The day with most customers is {most_customers}")
print(f"The day with the fewest customers is {fewest_customers}")

# Business analysis.

print("\n=== Business Analysis ===\n")
print("If some days are weaker, I can test a promotion or special offer on")
print("those days to attract more customers.")
