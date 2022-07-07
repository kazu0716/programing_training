N = int(input())
X = list(map(int, input().split()))
C = list(map(int, input().split()))
INF = pow(10, 18)

edge, rev = [[] for _ in range(N)], [[] for _ in range(N)]
in_cnt, out_cnt = [0]*N, [0]*N
for i in range(N):
    edge[i].append((X[i]-1, C[i]))
    rev[X[i]-1].append(i)
    in_cnt[X[i]-1] += 1
    out_cnt[i] += 1
# NOTE: delete needless branches
for cnt in (in_cnt, out_cnt):
    for dep in [i for i in range(N) if cnt[i] == 0]:
        stack = [dep]
        while stack:
            cur = stack.pop()
            for nxt, _ in edge[cur]:
                if cnt[cur] == 0:
                    stack.append(nxt)
                    cnt[nxt] -= 1
# NOTE: limit nodes by in and out cnt
ans, non_visited = 0, set([i for i in range(N) if in_cnt[i] > 0 and out_cnt[i] > 0])
while non_visited:
    dep = non_visited.pop()
    stack, min_cost = [dep], INF
    while stack:
        cur = stack.pop()
        for nxt, cost in edge[cur]:
            if nxt in non_visited:
                min_cost = min(min_cost, cost)
                non_visited.remove(nxt)
                stack.append(nxt)
            elif nxt == dep:
                min_cost = min(min_cost, cost)
    if min_cost != INF:
        ans += min_cost
print(ans)
