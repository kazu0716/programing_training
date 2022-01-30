from heapq import heappop, heappush

N, M = map(int, input().split())
H = tuple(map(int, input().split()))
edge = [[] for _ in range(N)]

for _ in range(M):
    U, V = map(int, input().split())
    edge[U-1].append(V-1)
    edge[V-1].append(U-1)

fun, heap = [-pow(10, 18)]*N, [(H[0], 0)]
fun[0], ans = 0, 0
while heap:
    cur_h, cur = heappop(heap)
    for nxt in edge[cur]:
        d = cur_h-H[nxt] if cur_h-H[nxt] >= 0 else -2*abs(cur_h-H[nxt])
        if fun[nxt] >= fun[cur]+d:
            continue
        fun[nxt] = fun[cur]+d
        ans = max(ans, fun[nxt])
        heappush(heap, (H[nxt], nxt))
print(ans)
