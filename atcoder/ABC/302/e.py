N, Q = map(int, input().split())
graph = [set() for _ in range(N)]
connected_set = set()
ans = []
for _ in range(Q):
    query = input().split()
    if query[0] == "1":
        u, v = map(lambda x: int(x) - 1, query[1:])
        graph[u].add(v)
        graph[v].add(u)
        connected_set.add(u)
        connected_set.add(v)
    else:
        v = int(query[1]) - 1
        for u in graph[v]:
            graph[u].remove(v)
            if not graph[u]:
                connected_set.remove(u)
        connected_set.discard(v)
        graph[v] = set()
    ans.append(N - len(connected_set))
print(*ans, sep="\n")
