from itertools import combinations

a, b, c, d, e, k = int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
for a1, a2 in combinations((a, b, c, d, e), 2):
    if abs(a1 - a2) > k:
        print(":(")
        exit()
print("Yay!")
