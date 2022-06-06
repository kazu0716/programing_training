from collections import defaultdict

N = int(input())
cnt, ans = defaultdict(int), 0
for i in range(1, N+1):
    j = 2
    while i > 1 and i >= j*j:
        while i % (j*j) == 0:
            i //= j*j
        j += 1
    cnt[i] += 1
ans = 0
for k in cnt:
    ans += cnt[k]*cnt[k]
print(ans)
