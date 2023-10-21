from collections import defaultdict

N = int(input())
cnt = defaultdict(int)
for _ in range(N):
    W, X = map(int, input().split())
    cnt[X] += W
ans = 0
for i in range(24):
    _sum = 0
    for j in cnt:
        s, t = (i + j) % 24, (i + j + 1) % 24
        if 9 <= s < t <= 18:
            _sum += cnt[j]
    ans = max(ans, _sum)
print(ans)
