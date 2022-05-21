from heapq import heappop, heappush

N, M = map(int, input().split())
INF = pow(10, 18)
edge = [[] for _ in range(N)]
for i in range(M):
    A, B, C = map(int, input().split())
    edge[A-1].append((B-1, C, i+1))
    edge[B-1].append((A-1, C, i+1))
dist, route = [INF] * N, [0]*N
dist[0], queue = 0, [(0, 0)]
while queue:
    _, cur = heappop(queue)
    for nxt, cost, i in edge[cur]:
        if dist[cur] + cost < dist[nxt]:
            dist[nxt] = dist[cur] + cost
            route[nxt] = i
            heappush(queue, (dist[nxt], nxt))
print(*route[1:])
