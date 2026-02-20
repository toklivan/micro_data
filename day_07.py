# Day 07
# Carte : Dictionnaire

visits_by_page = {
    "home": 320,
    "pricing": 85,
    "contact": 40,
    "blog": 150,
    "signup": 60,
}

# 1 Show all pages.

for pages in visits_by_page.keys():
    print(pages)

# 2 Display all the numbers of visits.

for nb_visits in visits_by_page.values():
    print(nb_visits)

# 3 Calculating the total visits.

total = 0
for nb_visits in visits_by_page.values():
    total += nb_visits
print("Total visits =", total)

# 4 Calculate the average of visits per page.

length = 0
for _ in visits_by_page:
    length += 1
average = total / length
print("Average of visits =", average)

# 5 Display the most visited page

max_page = None
max_visit = None
for page in visits_by_page:
    visits = visits_by_page[page]
    if max_visit is None or visits > max_visit:
        max_visit = visits
        max_page = page
print(f"The most visited page is: {max_page} with {max_visit}")

# 6 Display the least visited page

min_page = None
min_visit = None
for page in visits_by_page:
    visits = visits_by_page[page]
    if min_visit is None or visits < min_visit:
        min_visit = visits
        min_page = page
print(f"The least visited page is: {min_page} with {min_visit}")

# Business analysis.

print("\n=== Business Decision ===\n")
print("The page that deserve the most optimization \
      as a priority is the contact page.")
print("Because it generate the fewest visits.")
