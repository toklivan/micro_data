# Day 19
# Carte : Nettoyage simple

rows = [
    " product_A , 42 ",
    "product_B,30",
    " product_C ,55",
    "product_D , 18 ",
    " product_E,25 "
]

# 1 For each line, remove unnecessary spaces around the product and quantity.

clean_rows: list[str] = []

for line in rows:
    new_line = line.replace(" ", "")
    clean_rows.append(new_line)
print(clean_rows)

# 2 Separate product and quantity with 'split(",")'.

split_rows: list[list[str]] = []

for line in clean_rows:
    split_line = line.split(",")
    split_rows.append(split_line)
print(split_rows)

# 3 Store clean data in a 'clean_sales' dictionary.

clean_sales: dict[str, int] = {}

for parts in split_rows:
    key = parts[0]
    value = int(parts[1])
    clean_sales[key] = value

# 4 Calculate the total sales.

total: int = 0

for value in clean_sales.values():
    total += value
print(f"The total sales is {total}")

# 5 Displays the final content of dictionary.

for key in clean_sales:
    print(f"{key}: {clean_sales[key]}")

# Business analysis.

print("\n=== Business Analysis ===\n")
print("Poorly formatted data can distort a simple decision because it may \
be misread or miscompared, making you act on false information.")
