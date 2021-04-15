import sys
from collections import deque

N, Q = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
costs = [0]*(N+1)

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

for _ in range(Q):
    p, x = map(int, sys.stdin.readline().strip().split())
    costs[p] += x

q = deque()
q.append(1)

while q:
    v = q.pop()
    visited[v] = True

    for nxt in graph[v]:
        if not visited[nxt]:
            costs[nxt] += costs[v]
            q.append(nxt)

print(*costs[1:])
