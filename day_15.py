# Day 15
# Carte : Reecriture / simplification

rows = [
    "A,120",
    "B,95",
    "C,110",
    "D,0",
    "E,160"
]

d = {}
for r in rows:
    p = r.split(",")
    d[p[0]] = int(p[1])

t = 0
for k in d:
    t = t + d[k]

avg = t / len(d)

mk = None
mv = None
for k in d:
    if mv is None or d[k] > mv:
        mv = d[k]
        mk = k

print("Total:", t)
print("Average:", avg)
print("Best:", mk, mv)

# 1 Rewrite this code so that it is more readable
#   (clear variable names, clean structure).

# 2 Avoid unnecessary abbreviations (d ,r, p, t, mk, mv).

# 3 Keep exactly the same results in output.

# 4 Do not change the business logic, only clarity.

scores_by_key: dict = {}
for line in rows:
    parts = line.split(",")
    key = parts[0]
    score = int(parts[1])
    scores_by_key[key] = score

total: int = 0
for key in scores_by_key:
    total += scores_by_key[key]

average: float = total / len(scores_by_key)

best_key = None
best_score = None
for key in scores_by_key:
    score = scores_by_key[key]
    if best_score is None or scores_by_key[key] > best_score:
        best_score = scores_by_key[key]
        best_key = key

print("The total of score is: ", total)
print("The average of score is: ", average)
print(f"The best score is {best_key} with {best_score}")

print("\n=== Business Analysis ===\n")
print("Simplifying a code that works is important to \
make it easier for the whole team to understand, \
maintain and correct.")
