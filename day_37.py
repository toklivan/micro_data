# Day 37
# Carte : Liste

daily_revenue = [120, 80, 150, 200, 90, 170, 60]

# 1 Create a total_revenue variable and calculates the total with a loop.

# 2 Calculates the average revenue (average_revenue).

# 3 Shows average income.

# 4 Creates a low_days list.

# 5 Path daily_revenue and adds the days when the revenue is strictly below
#   average.

# 6 Displays low_days.

# 7 Count how many days are below average.

# 8 Show this number.

# 9 Find the day with the highest income without using max().

# 10 Displays this value.

total_revenue = 0

for revenue in daily_revenue:
    total_revenue += revenue

average_revenue = total_revenue / len(daily_revenue)

print(f"The average revenue is {average_revenue:.0f}")

low_days: list[int] = []

for revenue in daily_revenue:
    if revenue < average_revenue:
        low_days.append(revenue)

print(low_days)
print(f"There are {len(low_days)} days below average")

max_revenue = None

for revenue in daily_revenue:
    if max_revenue is None or revenue > max_revenue:
        max_revenue = revenue

print(f"The day with the highest income is {max_revenue}")

# Business question

print("\n=== Business answer ===\n")
print("Identifying days with below average income is")
print("important because it allows you to target low-income")
print("days amd apply actions to improve overall performance.")
