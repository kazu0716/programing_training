from collections import defaultdict

N, M = map(int, input().split())
cost = defaultdict(int)
for _ in range(N):
    A, B = map(int, input().split())
    cost[A] += B
ans = 0
for A in sorted(cost.keys()):
    if cost[A] > M:
        ans += A * M
        break
    ans += A * cost[A]
    M -= cost[A]
print(ans)
