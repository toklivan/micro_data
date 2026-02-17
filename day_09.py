# Day 09
# Carte : Nettoyage simple

rows = [
    " 2026-02-01 , 1200 ",
    "2026-02-02,950",
    " 2026-02-03, 1100",
    "2026-02-04 ,0 ",
    " 2026-02-05 , 1600 "
]

# 1 For each line, remove unnecessary spaces around the date and amount.

clean_rows: list = []

for line in rows:
    new_line = line.strip().replace(" ", "")
    clean_rows.append(new_line)
    print(new_line)
print(clean_rows)

# 2 Separate each clean line in date and amount with 'split(",")'.

split_rows: list = []

for line in clean_rows:
    parts = line.split(",")
    split_rows.append(parts)
print(split_rows)

# 3 Store the cleaned data in a 'revenue_clean' dictionary.

revenue_clean: dict = {}

for parts in split_rows:
    date = parts[0]
    amount = int(parts[1])
    revenue_clean[date] = amount

# 4 Calculates the total revenue from 'revenue_clean'.

total: int = 0

for amount in revenue_clean.values():
    total += amount
print(f"The total revenue is {total}")

# 5 Display the final content of 'revenue_clean'.

for day in revenue_clean:
    print(f"{day}: {revenue_clean[day]}")

# Business analysis.

print("\n=== Business Decision ===\n")
print("Without claening, you make decisions on false numbers.")
