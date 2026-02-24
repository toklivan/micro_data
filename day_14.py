# Day 14
# Carte : Nettoyage simple

rows = [
    " A , 120 ",
    "B,95",
    " C, 110",
    "D, 0 ",
    " E , 160 "
]

# 1 For each line, remove unnecessary space around the key and value.

clean_rows: list = []

for line in rows:
    new_line = line.strip().replace(" ", "")
    clean_rows.append(new_line)
print(clean_rows)

# 2 Separate each clean line in key and value with split(",").

split_rows: list = []

for line in clean_rows:
    split_line = line.split(",")
    split_rows.append(split_line)
print(split_rows)

# 3 Store the cleaned data in a 'scores_clean' dictionary.

score_clean: dict = {}

for parts in split_rows:
    key = parts[0]
    value = int(parts[1])
    score_clean[key] = value

# 4 Calculate the total of scores from 'score_clean'.

total: int = 0

for value in score_clean.values():
    total += value
print(f"The total score is : {total}")

# 5 Display the final content of 'score_clean'.

for key in score_clean:
    print(f"{key}: {score_clean[key]}")

# Business analysis.

print("\n=== Business Analysis ===\n")
print("Poorly formatted data can distort a simple decision because it may \
be misread or miscompared, making you act on false information.")
