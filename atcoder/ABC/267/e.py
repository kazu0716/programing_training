from heapq import heapify, heappop, heappush

N, M = map(int, input().split())
A = list(map(int, input().split()))

edge, costs = [[] for _ in range(N)], [0] * N
for _ in range(M):
    U, V = map(int, input().split())
    edge[U-1].append(V-1)
    edge[V-1].append(U-1)
    costs[U-1] += A[V-1]
    costs[V-1] += A[U-1]

hq, deleted, ans = [(c, i) for i, c in enumerate(costs)], [False] * N, 0
heapify(hq)
while hq:
    cost, cur = heappop(hq)
    if deleted[cur]:
        continue
    deleted[cur], ans = True, max(ans, cost)
    for nxt in edge[cur]:
        if deleted[nxt]:
            continue
        costs[nxt] -= A[cur]
        heappush(hq, (costs[nxt], nxt))
print(ans)
