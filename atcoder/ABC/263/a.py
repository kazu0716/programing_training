from collections import defaultdict

A, B, C, D, E = map(int, input().split())
cnt = defaultdict(int)
for n in (A, B, C, D, E):
    cnt[n] += 1
print("Yes" if sorted(cnt.values()) == [2, 3] else "No")
