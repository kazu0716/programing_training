from collections import deque
from heapq import heappop, heappush

Q = int(input())

queue = deque([])
heap = []
ans = []

for _ in range(Q):
    q = input().split()
    q[0] = int(q[0])
    if q[0] == 1:
        x = int(q[1])
        queue.append(x)
    elif q[0] == 2:
        if heap:
            ans.append(heappop(heap))
        else:
            ans.append(queue.popleft())
    else:
        while queue:
            heappush(heap, queue.pop())

print(*ans, sep="\n")
