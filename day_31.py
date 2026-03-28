# Day 31
# Carte : Liste

orders = [12.5, 8.0, 15.0, 22.5, 5.0, 18.0, 9.5]

# 1 Creates a variable 'total_revenue' and calculates the total of orders with
#   a loop.

# 2 Calculate the average basket 'average_order'.

# 3 Diaplay the average basket.

# 4 Create a 'large_orders' list.

# 5 Parcours orders and adds in 'large_orders' the orders strictly higher than
#   the average basket.

# 6 Display 'large_orders'.

# 7 Count how many orders are higher than the average basket.

# 8 Print this number.

# 9 Find the highest command without using max().

# 10 Print this value.

total_revenue: float = 0.0

for revenu in orders:
    total_revenue += revenu

average_order: float = total_revenue / len(orders)

print(f"The average basket is {average_order:.1f}")

large_orders: list[float] = []
for revenu in orders:
    if revenu > average_order:
        large_orders.append(revenu)

print(large_orders)
print(f"The number of orders are higher than the average basket is"
      f" {len(large_orders)}")

max_order = None
for revenu in orders:
    if max_order is None or max_order < revenu:
        max_order = revenu
print(f"The value of the highest command is {max_order}")

# Business question.

print("\n=== Business answer ===\n")
print("Identifying orders above the average basket is")
print("useful because it allows understanding what")
print("works well and replicating these behaviors to")
print("increase revenue.")
