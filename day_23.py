# Day 23
# Carte : Liste

daily_customers = [45, 52, 38, 60, 41, 55, 47]

# 1 Create a variable 'total_customers' and calculate the total of
# customers for the week with a loop.

# 2 Calculates the daily average of customers.

# 3 Displays the average.

# 4 Find the day with the fewest clients, without using min().

# 5 Displays the minimum number of customers.

# 6 Count how many days are below average.

# 7 Print this number.

total_customers: int = 0

for customers in daily_customers:
    total_customers += customers

daily_average: float = total_customers / len(daily_customers)

print(f"The daily average is {daily_average:.0f}")

min_day = None
for customers in daily_customers:
    if min_day is None or customers < min_day:
        min_day = customers

print(f"The days with the fewest clients is {min_day}")

days_below: int = 0
for customers in daily_customers:
    if customers < daily_average:
        days_below += 1

print(f"The number of days are below average is {days_below}")

# Business question.

print("\n=== Business answer ===\n")
print("If some days are weaker, I can test a promotion or special offer on")
print("those days to attract more customers.")
