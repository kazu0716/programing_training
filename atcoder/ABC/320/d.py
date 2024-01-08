from collections import defaultdict, deque
from typing import DefaultDict, List

N, M = map(int, input().split())
INF = pow(10, 18)
graph: List[DefaultDict[int, tuple]] = [defaultdict(tuple) for _ in range(N)]
for _ in range(M):
    A, B, X, Y = map(int, input().split())
    graph[A - 1][B - 1] = (X, Y)
    graph[B - 1][A - 1] = (-X, -Y)
pos: DefaultDict[int, tuple] = defaultdict(tuple)
pos[0] = (0, 0)
deq = deque([0])
while deq:
    cur = deq.popleft()
    cur_x, cur_y = pos[cur]
    for nxt in graph[cur].keys():
        if nxt in pos:
            continue
        nxt_x, nxt_y = cur_x + graph[cur][nxt][0], cur_y + graph[cur][nxt][1]
        pos[nxt] = (nxt_x, nxt_y)
        deq.append(nxt)
for i in range(N):
    if i in pos:
        print(*pos[i])
    else:
        print("undecidable")
