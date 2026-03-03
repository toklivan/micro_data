# Day 17
# Carte : Dictionnaire

expenses_by_category = {
    "rent": 1200,
    "utilities": 300,
    "supplies": 450,
    "marketing": 200,
    "transport": 150
}

# 1 Display all categories.

print("=== Categories ===")
for key in expenses_by_category:
    print(key)

# 2 Displays all amounts.

print("\n=== Amounts ===")
for value in expenses_by_category:
    print(expenses_by_category[value])

# 3 Calculate the total expenses.

total: int = 0
for expense in expenses_by_category:
    total += expenses_by_category[expense]
print(f"\nThe total of expenses is {total}")

# 4 Calculate the average expenditure by category.

length: int = 0
for _ in expenses_by_category:
    length += 1
average: float = total / length
print(f"\nThe average of expenditure is {average:.0f}")

# 5 Displays the most expensive category (name + amount).

high_category = None
high_expense = None
for key in expenses_by_category:
    if high_expense is None or expenses_by_category[key] > high_expense:
        high_expense = expenses_by_category[key]
        high_category = key
print(f"\nThe most expensive category is {high_category} with {high_expense}")

# 6 Displays the least expensive categoty (name + amount).

least_category = None
least_expense = None
for key in expenses_by_category:
    if least_expense is None or expenses_by_category[key] < least_expense:
        least_expense = expenses_by_category[key]
        least_category = key
print(f"The least expensive category is {least_category} with {least_expense}")

# Business analysis.

print("\n=== Business Analysis ===\n")
print("I must analyze the rent category first,\
because it is the highest expense and therefore the one that has the most\
impact on profitability.")
