from collections import defaultdict
from heapq import heappop, heappush

Q = int(input())
ans, cnt = [], defaultdict(int)
max_heap, min_heap = [], []
for _ in range(Q):
    query = input().split()
    if query[0] == "1":
        x = int(query[1])
        cnt[x] += 1
        heappush(max_heap, -x)
        heappush(min_heap, x)
    elif query[0] == "2":
        x, c = map(int, query[1:])
        cnt[x] -= min(c, cnt[x])
        if cnt[x] == 0:
            del cnt[x]
        while max_heap and -max_heap[0] not in cnt:
            heappop(max_heap)
        while min_heap and min_heap[0] not in cnt:
            heappop(min_heap)
    else:
        ans.append(-max_heap[0]-min_heap[0])
print(*ans, sep="\n")
