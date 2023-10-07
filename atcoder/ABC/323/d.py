from collections import defaultdict
from heapq import heapify, heappop, heappush

N = int(input())
slimes = []
cnt = defaultdict(int)
for _ in range(N):
    S, C = map(int, input().split())
    slimes.append(-S)
    cnt[S] += C
heapify(slimes)
is_calculated = defaultdict(bool)
while slimes:
    s = origin = -heappop(slimes)
    if is_calculated[s]:
        continue
    is_calculated[s] = True
    c = cnt[s]
    p = 0
    while s % 2 == 0:
        p += 1
        s //= 2
    if p > 0:
        cnt[s] += pow(2, p) * c
        heappush(slimes, -s)
        del cnt[origin]
ans = 0
for n in cnt.values():
    ans += bin(n)[2:].count("1")
print(ans)
