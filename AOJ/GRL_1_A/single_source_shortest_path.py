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
    V, E, r = map(int, input().split())
    edges = [[] for _ in range(V)]
    for _ in range(E):
        s, t, d = map(int, input().split())
        edges[s].append((t, d))

    for d in dijkstra(r, V, edges):
        if d == float("inf"):
            print("INF")
        else:
            print(d)


if __name__ == '__main__':
    main()
