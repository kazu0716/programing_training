_, K = map(int, input().split())
A = tuple(map(int, input().split()))
# NOTE: K * (K + 1) // 2 = 1 + 2 + 3 + ... + (K - 1) + K
ans = K * (K + 1) // 2
used_set = set()
for a in A:
    if a <= K and a not in used_set:
        ans -= a
        used_set.add(a)
print(ans)
