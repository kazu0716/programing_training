from heapq import heappop, heappush

_, K = map(int, input().split())
A = set(map(int, input().split()))
heap = [0]
total, total_set = [], set()
while len(total) < K:
    cur = heappop(heap)
    if cur > 0:
        total.append(cur)
    for a in A:
        if cur + a not in total_set:
            heappush(heap, cur + a)
            total_set.add(cur + a)
print(total[-1])
