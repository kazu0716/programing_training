from heapq import heappop, heappush

INF = float("inf")


def dijkstra(s, n, adj):
    dist = [INF] * n
    hq = [(0, s)]
    dist[s] = 0
    seen = [False] * n
    while hq:
        v = heappop(hq)[1]
        seen[v] = True
        for to, cost in adj[v]:
            if not seen[to] and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist


def main():
    N, M = map(int, input().split())
    adj, ans, out = [[]for _ in range(
        N)], [INF] * N, [[INF] * N for _ in range(N)]

    for _ in range(M):
        a, b, c = map(int, input().split())
        adj[a-1].append((b-1, c))
        if a-1 == b-1:
            ans[a-1] = c

    for s in range(N):
        for dst, cost in enumerate(dijkstra(s, N, adj)):
            if s != dst:
                out[s][dst] = min(out[s][dst], cost)

    for i, o in enumerate(out):
        for j, cost in enumerate(o):
            if cost != INF:
                ans[i] = min(ans[i], cost + out[j][i])

    for a in ans:
        if a == INF:
            print(-1)
        else:
            print(a)


if __name__ == '__main__':
    main()
