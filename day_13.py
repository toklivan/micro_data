# key 13
# Carte : CSV

rows = [
    "A,120",
    "B,95",
    "C,110",
    "D,0",
    "E,160"
]

# 1 For each line, separate the key (A, B, C...) and the value with split(",").

for line in rows:
    parts = line.split(",")

# 2 Store this data in scores_by_key dictionary (key -> value in int).

scores_by_key: dict = {}

for line in rows:
    parts = line.split(",")
    scores_by_key[parts[0]] = int(parts[1])
print(scores_by_key)

# 3 Calculate the total of the scores.

total: int = 0
for score in scores_by_key.values():
    total += score
print("The total of the scores is :", total)

# 4 Calculate the average of the scores.

length: int = 0
for _ in scores_by_key.values():
    length += 1
average: float = total / length
print("The average of the scores is :", average)

# 5 Displays the key with the highest scores.

max_key = None
max_score = None

for key in scores_by_key:
    scores: int = scores_by_key[key]
    if max_score is None or scores > max_score:
        max_score = scores
        max_key = key
print(f"The key with the highest score is : {max_key} with {max_score}")

# 6 Displays the key with the lowest scores.

min_key = None
min_score = None

for key in scores_by_key:
    scores: int = scores_by_key[key]
    if min_score is None or scores < min_score:
        min_score = scores
        min_key = key
print(f"The key with the lowest score is : {min_key} with {min_score}")

# Business Analysis.

print("\n=== Business Analysis ===\n")
print("The key that deserves my attention is key D, \
because its score is at zero.")
