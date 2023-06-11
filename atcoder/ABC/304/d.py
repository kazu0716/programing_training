from bisect import bisect_left
from collections import defaultdict

W, H = map(int, input().split())
N = int(input())
pq = [tuple(map(int, input().split())) for _ in range(N)]
A = int(input())
a = [0] + list(map(int, input().split())) + [W]
B = int(input())
b = [0] + list(map(int, input().split())) + [H]
cnt = defaultdict(int)
for p, q in pq:
    idx = (bisect_left(a, p), bisect_left(b, q))
    cnt[idx] += 1
print(0 if len(cnt) < (A + 1) * (B + 1) else min(cnt.values()), max(cnt.values()))
