# Day 36
# Carte : Dictionnaire

orders = [
    {"customer": "Alice", "amount": 25.0},
    {"customer": "Bob", "amount": 15.0},
    {"customer": "Alice", "amount": 35.0},
    {"customer": "Charlie", "amount": 20.0},
    {"customer": "Bob", "amount": 30.0}
]

# 1 Create revenue_by_customer dictionary.

# 2 Browse the orders list.

# 3 For each order: - retrieve customer.
#                   - retrieve amount.

# 4 Adds up amounts per customer.

# 5 Display revenue_by_customer.

# 6 Calculates total income.

# 7 Show this total.

# 8 Calculates the average revenue per customer.

# 9 Shows this average income.

# 10 Find the customer who spent the most (without using max()).

# 11 Shows this customer and its amount.

revenue_by_customer: dict = {}

for order in orders:
    customer = order["customer"]
    amount = order["amount"]
    revenue_by_customer[customer] = revenue_by_customer.get(customer, 0) + amount

print(revenue_by_customer)

total_revenue = 0.0

for value in revenue_by_customer.values():
    total_revenue += value

print(f"The total income is {total_revenue}")

avg_income = total_revenue / len(revenue_by_customer)

print(f"The average income is {avg_income:.2f}")

best_customer = None
best_amount = None
for customer, value in revenue_by_customer.items():
    if best_amount is None or value > best_amount:
        best_amount = amount
        best_customer = customer

print(f"The customer who spent the most is {best_customer} with {best_amount}")

# Business question

print("\n=== Business answer ===\n")
print("Identifying the best customers is essential")
print("because it allows you to focus efforts on those")
print("that generate the most value and increase")
print("profitability.")
