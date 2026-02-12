# Day 08
# Carte : CSV

rows = [
    "2026-02-01,1200",
    "2026-02-02,950",
    "2026-02-03,1100",
    "2026-02-04,0",
    "2026-02-05,1600"
]

# 1 For each line, separate the date and amount with 'split(",")'.

for line in rows:
    parts = line.split(",")
    print(parts)

# 2 Stores this data in a dictionary 'revenue_by_day' (date -> amount in int).

revenue_by_day = {}

for line in rows:
    parts = line.split(",")
    revenue_by_day[parts[0]] = int(parts[1])
print(revenue_by_day)

# 3 Calculate the total revenue.

total = 0
for value in revenue_by_day.values():
    total += value
print("The total revenue is:", total)

# 4 Calculates the average revenue per day.

length = 0
for _ in revenue_by_day:
    length += 1
average = total / length
print("The average revenue per day is:", average)

# 5 Displays the day with the highest revenue.

max_day = None
max_revenue = None
for day in revenue_by_day:
    revenue = revenue_by_day[day]
    if max_revenue is None or revenue > max_revenue:
        max_revenue = revenue
        max_day = day
print(f"The day with the highest revenue is {max_day} with {max_revenue}")

# 6 Displays the day with the lowest revenue.

min_day = None
min_revenue = None
for day in revenue_by_day:
    revenue = revenue_by_day[day]
    if min_revenue is None or revenue < min_revenue:
        min_revenue = revenue
        min_day = day
print(f"The day with the lowest revenue is {min_day} with {min_revenue}")

# Business analysis.

print("\n=== Business Decision ===\n")
print(f"The day that requires immediate action is {min_day}.")
print("Because this day revenue is at 0.")