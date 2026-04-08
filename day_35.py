# Day 35
# Carte : CSV

rows = [
    "date,produit,quantite",
    "2024-01-01,apple,3",
    "2024-01-01,banana,2",
    "2024-01-02,apple,4",
    "2024-01-02,orange,1",
    "2024-01-03,banana,5",
    "2024-01-03,apple,2"
]

# 1 Create sales_by_date dictionary.

# 2 Ignore the header.

# 3 Browse the remaining lines>

# 4 For each line: - use split(",").
#                  - retrieve date, product, quantity

# 5 Convert quantity to int.

# 6 Add the quantities by date (not by product).

# 7 Display sales_by_date.

# 8 Find the day with the most sales (without max()).

# 9 Displays the corresponding date and quantity.

sales_by_date: dict = {}

for row in rows[1:]:
    parts = row.split(",")
    date = parts[0]
    product = parts[1]
    quantity = int(parts[2])
    sales_by_date[date] = sales_by_date.get(date, 0) + quantity

print(sales_by_date)

max_day = None
max_quantity = None

for day, quantity in sales_by_date.items():
    if max_quantity is None or quantity > max_quantity:
        max_quantity = quantity
        max_day = day

print(f"The day with the most sales is {max_day} with {max_quantity}")

# Business question

print("\n=== Business answer ===\n")
print("Identifying the days with the most sales is useful")
print("because it allows for strengthening resources and")
print("actions on these days to maximize revenue.")
