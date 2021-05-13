from heapq import heappop, heappush
from sys import stdin

INF = pow(10, 16)


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
    readline = stdin.readline
    N, M = map(int, readline().split())

    range_n = range(N)
    adj = [[] for _ in range_n]
    ans, costs = [INF] * N, [[INF] * N for _ in range_n]

    for _ in range(M):
        a, b, c = map(int, readline().split())
        adj[a-1].append((b-1, c))
        if a == b:
            ans[a-1] = min(ans[a-1], c)

    for s in range_n:
        dist = dijkstra(s, N, adj)
        for d, cost in enumerate(dist):
            if s != d:
                costs[s][d] = cost

    for s in range_n:
        for d in range_n:
            if s == d:
                continue
            ans[d] = min(ans[d], costs[s][d] + costs[d][s])

    for i, a in enumerate(ans):
        if a == INF:
            a[i] = -1

    print(*ans, sep="\n")


if __name__ == '__main__':
    main()
