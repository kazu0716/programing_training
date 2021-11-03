from collections import defaultdict

N, M = map(int, input().split())
cnt = defaultdict(int)

for A in map(int, input().split()):
    cnt[A] += 1
for _ in range(M):
    B, C = map(int, input().split())
    cnt[C] += B

ans = 0
for key in sorted(cnt.keys(), reverse=True):
    n = cnt[key]
    if N <= n:
        ans += key*N
        break
    else:
        ans += key*n
        N -= n

print(ans)
