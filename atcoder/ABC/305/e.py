from heapq import heapify, heappop, heappush

N, M, K = map(int, input().split())
INF = pow(10, 18)
edge = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)
guards = [-1] * N
for _ in range(K):
    p, h = map(int, input().split())
    guards[p - 1] = h
guard_hp = [INF] * N
heap = [(-h, p) for p, h in enumerate(guards) if h > 0]
heapify(heap)
while heap:
    hp, cur = heappop(heap)
    if guard_hp[cur] <= hp:
        continue
    guard_hp[cur] = hp
    for nxt in edge[cur]:
        nxt_hp = max(-hp - 1, guards[nxt])
        if nxt_hp < 0 or guard_hp[nxt] <= nxt_hp:
            continue
        guard_hp[nxt] = nxt_hp
        heappush(heap, (-nxt_hp, nxt))
ans = [i + 1 for i, hp in enumerate(guard_hp) if hp < INF]
print(len(ans))
print(*ans)
