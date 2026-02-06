# Day 04
# Carte : Nettoyage simple

data = [
    " lundi , 120 ",
    "mardi,95",
    " mercredi, 110",
    "jeudi ,0",
    "vendredi, 160"
]

print("=== Day 04 - Easy cleaning ===\n")
# 1 For each line, remove unnecessary spaces around the day and the sale.
# 2 Transform each clean line into day (string) and sale (int).
# 3 Stores the cleaned data in a 'sales_clean' dictionary.

sales_clean = {}

for line in data:
    parts = line.split(",")
    day = parts[0].strip()
    sale_str = parts[1].strip()
    sale = int(sale_str)
    sales_clean[day] = sale

# 4 Calculate the total of sales from 'sales_clean'.

total = 0

for value in sales_clean.values():
    total += value

print(f"Total sales = {total}\n")

# 5 Display the final content of 'sales_clean'.

for key in sales_clean:
    print(key, sales_clean[key])

# Business analysis
print("\n=== Business analysis ===\n")
print("If the data is dirty, the calculations are false.")
print("As a result, the decisions taken will be bad.")
