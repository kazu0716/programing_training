from itertools import combinations

N, M = map(int, input().split())
ans = 0

if N >= 2:
    ans += len(list(combinations(range(N), 2)))

if M >= 2:
    ans += len(list(combinations(range(M), 2)))

print(ans)
