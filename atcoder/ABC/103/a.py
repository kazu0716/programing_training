from itertools import permutations

A1, A2, A3 = map(int, input().split())
ans = pow(10, 9)
for a1, a2, a3 in permutations((A1, A2, A3), 3):
    ans = min(ans, abs(a2 - a1) + abs(a3 - a2))
print(ans)
