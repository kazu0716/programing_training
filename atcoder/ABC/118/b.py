from collections import defaultdict

N, M = map(int, input().split())
cnt = defaultdict(int)
for _ in range(N):
    KA = tuple(map(int, input().split()))
    for a in KA[1:]:
        cnt[a] += 1
print(len([v for v in cnt.values() if v >= N]))
