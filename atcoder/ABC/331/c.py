from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
cnt = defaultdict(int)
for a in A:
    cnt[a] += 1
s = 0
total = defaultdict(int)
for k in sorted(cnt.keys(), reverse=True):
    total[k] = s
    s += k * cnt[k]
print(*[total[a] for a in A])
