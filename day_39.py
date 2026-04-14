# Day 39
# Carte : CSV

rows = [
    "customer,produit,amount",
    "Alice,apple,12.0",
    "Bob,banana,8.0",
    "Alice,orange,5.0",
    "Bob,apple,7.0",
    "Charlie,banana,10.0",
    "Alice,banana,6.0"
]

# 1 Creates a revenue_by_customer dictionary.

# 2 Ignore the header.

# 3 Browse the remaining rows.

# 4 For each row : - use split(",").
#                  - retrieves customer, product, amount.

# 5 Convert amount to float.

# 6 Adds up amounts per customer.

# 7 Display revenue_by_customer.

# 8 Find the customer with the lowest income (without using min()).

# 9 Shows this customer and its amount.

# 10 Calculates total income.

# 11 Show this total.

revenue_by_customer: dict[str, float] = {}

for row in rows[1:]:
    parts = row.split(",")
    customer = parts[0]
    product = parts[1]
    amount = float(parts[2])
    revenue_by_customer[customer] = revenue_by_customer.get(customer, 0.0) + amount

print(revenue_by_customer)

min_customer = None
min_amount = None
total_revenue = 0.0

for customer, value in revenue_by_customer.items():
    total_revenue += value
    if min_amount is None or min_amount > value:
        min_amount = value
        min_customer = customer

print(f"The customer with the lowest income is {min_customer} with {min_amount}")

print(f"The total income is {total_revenue}")

# Business question

print("\n=== Business answer ===\n")
print("Identifying the customers who spend the least is")
print("useful beacuse it allows you to implement targeted")
print("actions to make them buy more and increase sales.")
