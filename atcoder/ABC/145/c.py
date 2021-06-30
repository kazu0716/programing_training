from itertools import permutations
from math import factorial, sqrt

N = int(input())
town = []
s = 0.0

for _ in range(N):
    x, y = map(int, input().split())
    town.append((x, y))

perm = permutations(range(N))

for p in perm:
    for i in range(len(p)-1):
        x1, y1 = town[p[i]][0], town[p[i]][1]
        x2, y2 = town[p[i+1]][0], town[p[i+1]][1]
        d2 = (x1 - x2) ** 2 + (y1 - y2) ** 2
        s += sqrt(d2)

print(s/factorial(N))
