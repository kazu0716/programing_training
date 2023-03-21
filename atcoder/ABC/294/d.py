from collections import defaultdict
from heapq import heapify, heappop, heappush

N, Q = map(int, input().split())
not_called, called = [i for i in range(1, N + 1)], []
is_gone = defaultdict(bool)
heapify(not_called)
ans = []
for _ in range(Q):
    query = input().split()
    if query[0] == "1":
        heappush(called, heappop(not_called))
    elif query[0] == "2":
        is_gone[int(query[1])] = True
    else:
        while called:
            if not is_gone[called[0]]:
                ans.append(called[0])
                break
            heappop(called)
print(*ans, sep="\n")
