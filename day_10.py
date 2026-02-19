# Day 10
# Carte : Reecriture / simplification

# Code original

rows = [
    "2026-02-01,1200",
    "2026-02-02,950",
    "2026-02-03,1100",
    "2026-02-04,0",
    "2026-02-05,1600"
]

revenue = {}
for r in rows:
    p = r.split(",")
    revenue[p[0]] = int(p[1])

t = 0
for k in revenue:
    t = t + revenue[k]

avg = t / len(revenue)

md = None
mv = None
for k in revenue:
    if mv is None or revenue[k] > mv:
        mv = revenue[k]
        md = k

print("Total:", t)
print("Average:", avg)
print("Best day:", md, mv)

# Code simplifie

revenue_by_day: dict = {}
for line in rows:
    parts = line.split(",")
    date = parts[0]
    amount = int(parts[1])
    revenue_by_day[date] = amount

total: int = 0
for amount in revenue_by_day.values():
    total += amount

average = total / len(revenue_by_day)

best_day = None
best_amount = None
for date in revenue_by_day:
    amount = revenue_by_day[date]
    if best_amount is None or amount > best_amount:
        best_amount = amount
        best_day = date

print("Total:", total)
print("Average:", average)
print("Best day:", best_day, best_amount)

# Business analysis.

print("\n=== Business Decision ===\n")
print("We rewrite working code so it stays readable \
      and maintainable for the team.")
