# Day 06
# Carte : Liste

temps_attente = [5, 12, 7, 3, 20, 9, 4]

# 1 Display all waiting times.

for time in temps_attente:
    print(time)

# 2 Calculate the total waiting time.

total = 0
for time in temps_attente:
    total += time
print("Total waiting time:", total)

# 3 Calculate the average waiting time.

length = 0
for time in temps_attente:
    length += 1
average = total / length
print(f"Average waiting time: {average:.2f}")

# 4 Displays the maximum waiting time.

max_wait = temps_attente[0]
for time in temps_attente:
    if time > max_wait:
        max_wait = time
print("Max waiting time:", max_wait)

# 5 Displays the minimum waiting time.

min_wait = temps_attente[0]
for time in temps_attente:
    if time < min_wait:
        min_wait = time
print("Min waiting time:", min_wait)

# Business analysis.

print("\n=== Business Decision ===\n")
print("Open an additional fund when the wait exceeds a threshold")
