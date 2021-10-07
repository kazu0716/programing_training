from collections import deque
from itertools import accumulate

N, K = map(int, input().split())
P = list(map(int, input().split()))

s = list(accumulate(range(1, 1001)))
deq = deque(P[0:K])
ret = sum([s[p-1]/p for p in deq])
ans = ret

for i in range(K, N):
    p, q = P[i], deq.popleft()
    deq.append(p)
    pb1, pb2 = s[p-1]/p, s[q-1]/q
    ret += pb1 - pb2
    ans = max(ans, ret)

print(ans)
