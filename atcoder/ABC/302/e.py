N, Q = map(int, input().split())
graph = [set() for _ in range(N)]
ans = []
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        u, v = query[1] - 1, query[2] - 1
        if not graph[u]:
            N -= 1
        graph[u].add(v)
        if not graph[v]:
            N -= 1
        graph[v].add(u)
    else:
        v = query[1] - 1
        for u in graph[v]:
            graph[u].remove(v)
            if not graph[u]:
                N += 1
        if graph[v]:
            N += 1
        graph[v] = set()
    ans.append(N)
print(*ans, sep="\n")
