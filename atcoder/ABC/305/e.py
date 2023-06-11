from collections import deque

N, M, K = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)
guards = [-1] * N
for _ in range(K):
    p, h = map(int, input().split())
    guards[p - 1] = h
cost = [-1] * N
for root, ini_hp in sorted([(p, h) for p, h in enumerate(guards) if h > 0], key=lambda x: x[1], reverse=True):
    if cost[root] >= ini_hp:
        continue
    deq = deque([(root, ini_hp)])
    cost[root] = ini_hp
    while deq:
        cur, hp = deq.popleft()
        for nxt in edge[cur]:
            nxt_hp = max(hp - 1, guards[nxt])
            if nxt_hp < 0 or cost[nxt] >= nxt_hp:
                continue
            cost[nxt] = nxt_hp
            deq.append((nxt, nxt_hp))
ans = [i + 1 for i, c in enumerate(cost) if c > -1]
print(len(ans))
print(*ans)
