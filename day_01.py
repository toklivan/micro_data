# Day 01
# Carte : Liste

nombres = [3, 7, 10, 2]
print(nombres)
print(nombres[0])
print(nombres[len(nombres) - 1])

# Une liste = une suite d'elements
# Chaque element a un index
# L'index commence toujours a 0
# L'ordre = ordre d'ecriture, pas valeur

print(len(nombres))
print(nombres[-1])

# [0] -> premier element
# [-1] -> dernier element
# len() -> combien il y a d'elements
# len() - 1 -> index du dernier element

print(nombres[1:3])

# liste[a:b]
# on commence a l'index a (inclus)
# on s'arrete avant l'index b (exclu)

print(nombres[:2])
print(nombres[2:])
print(nombres[::2])

# liste[a:b:c]
# c represente le pas avec lequel on avance dans l'index
