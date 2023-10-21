from heapq import heappop, heappush


def dijkstra(s, n, adj, is_car):
    dist = [INF] * n
    hq = [(0, s)]
    dist[s] = 0
    seen = [False] * n
    while hq:
        v = heappop(hq)[1]
        seen[v] = True
        for to, d in adj[v]:
            cost = d * A if is_car else d * B + C
            if not seen[to] and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist


N, A, B, C = map(int, input().split())
graph = [[] for _ in range(N)]
for i in range(N):
    for j, d in enumerate(map(int, input().split())):
        graph[i].append((j, d))
        graph[j].append((i, d))
INF = pow(10, 18)
car_dist = dijkstra(0, N, graph, True)
rev_train_dist = dijkstra(N - 1, N, graph, False)
ans = car_dist[-1]
for i in range(N):
    ans = min(ans, car_dist[i] + rev_train_dist[i])
print(ans)
