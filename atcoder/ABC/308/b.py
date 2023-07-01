from collections import defaultdict

N, M = map(int, input().split())
C = list(input().split())
D = list(input().split())
P = list(map(int, input().split()))
cost = defaultdict(int)
for i, d in enumerate(D):
    cost[d] = P[i + 1]
ans = 0
for c in C:
    ans += P[0] if c not in cost else cost[c]
print(ans)
