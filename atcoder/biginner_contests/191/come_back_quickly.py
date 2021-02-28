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
    range_n = range(N)
    adj = [[] for _ in range_n]
    ans, costs = [INF] * N, [[INF] * N for _ in range_n]

    for _ in range(M):
        a, b, c = map(int, input().split())
        adj[a-1].append((b-1, c))
        if a == b:
            ans[a-1] = c

    for s in range_n:
        for d, cost in enumerate(dijkstra(s, N, adj)):
            if s != d:
                costs[s][d] = min(costs[s][d], cost)

    for s in range_n:
        for d in range_n:
            if s != d:
                ans[d] = min(ans[d], costs[s][d] + costs[d][s])

    for a in ans:
        if a == INF:
            print(-1)
        else:
            print(a)


if __name__ == '__main__':
    main()
