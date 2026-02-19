# Day 11
# Carte : Liste

orders = [3, 1, 4, 2, 6, 2, 5]

# 1 Displays all numbers of commands.

for orders_count in orders:
    print(orders_count)

# 2 Calculate the total of orders.

total: int = 0
for orders_count in orders:
    total += orders_count
print(f"The total of orders is : {total}")

# 3 Calculate the average number of orders.

average: float = total / len(orders)
print(f"The average number of orders is : {average:.2f}")

# 4 Displays the maximum number of orders.

max_orders = None
for orders_count in orders:
    if max_orders is None or orders_count > max_orders:
        max_orders = orders_count
print(f"The maximum number of orders is : {max_orders}")

# 5 Displays the minimum number of orders.

min_orders = None
for orders_count in orders:
    if min_orders is None or orders_count < min_orders:
        min_orders = orders_count
print(f"The minimum number of orders is : {min_orders}")
