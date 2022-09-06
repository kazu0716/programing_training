def can_traverse(c: int, costs: list) -> bool:
    stack, exsiting = set([i for i in range(N) if cost[i] <= c]), set([i for i in range(N)])
    while stack:
        cur = stack.pop()
        exsiting.remove(cur)
        for aj in edge[cur]:
            if aj not in exsiting:
                continue
            costs[aj] -= A[cur]
            if costs[aj] <= c and aj not in stack:
                stack.add(aj)
    return not exsiting


N, M = map(int, input().split())
A = list(map(int, input().split()))

edge, cost = [[] for _ in range(N)], [0] * N
for _ in range(M):
    U, V = map(int, input().split())
    edge[U-1].append(V-1)
    edge[V-1].append(U-1)
    cost[U-1] += A[V-1]
    cost[V-1] += A[U-1]
low, high = -1, max(cost)
while high - low > 1:
    mid = (low + high) // 2
    if can_traverse(mid, cost.copy()):
        high = mid
    else:
        low = mid
print(high)
