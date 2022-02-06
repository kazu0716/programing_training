from heapq import heappop, heappush


def dijkstra(s):
    finds, dist = [False]*N, [INF]*N
    dist[s] = 0
    queue = [(0, s)]
    while queue:
        _, cur = heappop(queue)
        finds[cur] = True
        for nxt, cost in edge[cur]:
            if not finds[nxt] and dist[nxt] > dist[cur]+cost:
                dist[nxt] = dist[cur]+cost
                heappush(queue, (dist[nxt], nxt))
    return dist


N, M = map(int, input().split())
INF = pow(10, 18)
edge = [[] for _ in range(N)]
for _ in range(M):
    A, B, C = map(int, input().split())
    edge[A-1].append((B-1, C))
    edge[B-1].append((A-1, C))

dist1, dist2 = dijkstra(0), dijkstra(N-1)
print(*[dist1[k]+dist2[k] for k in range(N)], sep="\n")
