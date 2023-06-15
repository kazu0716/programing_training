from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))
cnt = defaultdict(int)
cnt[0] = 1
ans, s = 0, 0
for i in range(N):
    s += A[i]
    ans += cnt[s % M]
    cnt[s % M] += 1
print(ans)
