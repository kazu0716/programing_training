from collections import deque

N, M = map(int, input().split())
p = tuple(map(int, input().split()))
graph = [[] for _ in range(N)]
for i, pp in enumerate(p):
    graph[pp - 1].append(i + 1)
compensated = [-1] * N
for _ in range(M):
    x, y = map(int, input().split())
    compensated[x - 1] = max(compensated[x - 1], y)
deq = deque([(0, compensated[0])])
while deq:
    cur, c = deq.popleft()
    for nxt in graph[cur]:
        compensated[nxt] = max(compensated[nxt], c - 1)
        deq.append((nxt, compensated[nxt]))
print(len([c for c in compensated if c > -1]))
