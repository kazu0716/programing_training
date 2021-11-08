from heapq import heappop, heappush

N, M, X, Y = map(int, input().split())
INF = pow(10, 18)
edge = [[] for _ in range(N+1)]

for _ in range(M):
    A, B, T, K = map(int, input().split())
    edge[A].append((B, T, K))
    edge[B].append((A, T, K))

time = [INF]*(N+1)
time[X] = 0
heap, finds = [(0, X)], [False]*(N+1)

while heap:
    now, cur = heappop(heap)
    if now > time[cur]:
        continue
    finds[cur] = True
    if cur == Y:
        break
    for nxt, t, k in edge[cur]:
        cost = now + t if now % k == 0 else k*(now//k+1) + t
        if finds[nxt] or cost >= time[nxt]:
            continue
        time[nxt] = cost
        heappush(heap, (time[nxt], nxt))

ans = time[Y]
if ans == INF:
    print(-1)
else:
    print(ans)
