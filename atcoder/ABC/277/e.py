from collections import deque

N, M, K = map(int, input().split())
INF = pow(10, 9)
edge_ini, edge_on = [set() for _ in range(N)], [set() for _ in range(N)]
for _ in range(M):
    u, v, a = map(int, input().split())
    if a == 1:
        edge_ini[u - 1].add(v - 1)
        edge_ini[v - 1].add(u - 1)
    else:
        edge_on[u - 1].add(v - 1)
        edge_on[v - 1].add(u - 1)
S = set(map(lambda x: int(x) - 1, input().split()))
visited_ini, visited_on = set([0]), set()
queue = deque([(0, 0, True)])
ans = INF
while queue:
    cur, cnt, status = queue.popleft()
    for i in range(2 if cur in S else 1):
        status = not status if i == 1 else status
        edge = edge_ini if status else edge_on
        visited = visited_ini if status else visited_on
        for nxt in edge[cur]:
            if nxt in visited or cnt + 1 >= ans:
                continue
            visited.add(nxt)
            if nxt == N - 1:
                ans = min(ans, cnt + 1)
                continue
            queue.append((nxt, cnt + 1, status))
print(ans if ans < INF else -1)
