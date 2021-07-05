from bisect import bisect_left
from math import factorial

P = int(input())
costs = [factorial(n) for n in range(1, 11)]
ans = 0

while P != 0:
    if P in costs:
        ans += 1
        break

    left = bisect_left(costs, P)
    q, mod = divmod(P, costs[left-1])
    P = mod
    ans += q

print(ans)
