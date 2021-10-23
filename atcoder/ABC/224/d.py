from collections import deque

M = int(input())
edge = [[] for _ in range(9)]
for _ in range(M):
    u, v = map(int, input().split())
    edge[u-1].append(v-1)
    edge[v-1].append(u-1)
P = list(map(int, input().split()))
GOAL = "123456789"
EMPTY = "9"

tmp = [EMPTY]*9
for i, e in enumerate(P):
    tmp[e-1] = str(i+1)
ini = "".join(tmp)
queue = deque([ini])
dist = {ini: 0}

while queue:
    cur = queue.popleft()
    if cur == GOAL:
        break
    dst = cur.index(EMPTY)
    for src in edge[dst]:
        tmp = list(cur)
        tmp[dst], tmp[src] = cur[src], EMPTY
        nxt = "".join(tmp)
        if nxt in dist:
            continue
        dist[nxt] = dist[cur] + 1
        queue.append(nxt)

if GOAL in dist:
    print(dist[GOAL])
else:
    print(-1)
