from heapq import heappop, heappush, heappushpop
from typing import List

X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = sorted(list(map(int, input().split())), reverse=True)
AB = [a + b for a in A for b in B]
heap: List[int] = []
for ab in AB:
    for c in C:
        if len(heap) < K:
            heappush(heap, ab + c)
            continue
        if heap[0] > ab + c:
            break
        heappushpop(heap, ab + c)
print(*[heappop(heap) for _ in range(K)][::-1], sep="\n")
