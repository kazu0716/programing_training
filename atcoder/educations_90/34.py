from collections import defaultdict

N, K = map(int, input().split())
A = tuple(map(int, input().split()))

l, r = 0, 0
kinds, ans = defaultdict(int), 0
while N-l >= ans:
    while len(kinds.keys()) <= K:
        ans = max(ans, r-l)
        if r >= N:
            break
        kinds[A[r]] += 1
        r += 1
    kinds[A[l]] -= 1
    if kinds[A[l]] == 0:
        del kinds[A[l]]
    l += 1
print(ans)
