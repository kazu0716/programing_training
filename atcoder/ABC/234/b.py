from itertools import combinations
from math import sqrt

N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]
ans = 0

for p1, p2 in combinations(P, 2):
    ans = max(ans, abs(p1[0]-p2[0])**2 + abs(p1[1]-p2[1])**2)
print(sqrt(ans))
