from collections import defaultdict, deque

N = int(input())
edge = [[] for _ in range(N+1)]
inputs = []
color = [defaultdict(int) for _ in range(N+1)]
k = 0

for _ in range(N-1):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)
    inputs.append((a, b))
    k = max(k, len(edge[a]), len(edge[b]))

deq = deque([(1, -1)])
finds = [False]*(N+1)

while deq:
    cur, c = deq.popleft()
    finds[cur] = True
    c = (c+1) % k
    for nxt in edge[cur]:
        if finds[nxt]:
            continue
        color[cur][nxt] = c
        color[nxt][cur] = c
        deq.append((nxt, c))
        c = (c+1) % k

ans = [k]
for a, b in inputs:
    ans.append(color[a][b]+1)

print(*ans, sep="\n")
