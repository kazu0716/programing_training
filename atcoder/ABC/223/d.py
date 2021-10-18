from heapq import heappop, heappush

N, M = map(int, input().split())

edge = [[] for _ in range(N)]
cnt = [0] * N

for _ in range(M):
    A, B = map(int, input().split())
    edge[A-1].append(B-1)
    cnt[B-1] += 1

heap = []
for i in range(N):
    if cnt[i] == 0:
        heappush(heap, i)

ans = []
while heap:
    cur = heappop(heap)
    ans.append(cur+1)
    for nxt in edge[cur]:
        cnt[nxt] -= 1
        if cnt[nxt] == 0:
            heappush(heap, nxt)

if len(ans) < N:
    print(-1)
else:
    print(*ans)
