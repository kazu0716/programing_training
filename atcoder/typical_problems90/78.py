from heapq import heappop, heappush

N, M = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    heappush(edge[a-1], b-1)
    heappush(edge[b-1], a-1)
ans = 0
for i in range(N):
    if not edge[i]:
        continue
    j = heappop(edge[i])
    if j < i and not edge[i]:
        ans += 1
    elif edge[i] and j < i and i < heappop(edge[i]):
        ans += 1
print(ans)
