N, M = map(int, input().split())
A = list(map(int, input().split()))

edge = [[] for _ in range(N+1)]
finds = [False]*(N+1)
ans = -pow(10, 12)

for _ in range(M):
    X, Y = map(int, input().split())
    edge[X].append(Y)

for ini, _ in sorted([(i+1, n)for i, n in enumerate(A)], key=lambda x: x[1]):
    if not edge[ini]:
        continue
    stack, finds[ini] = [ini], True
    while stack:
        cur = stack.pop()
        if not edge[cur]:
            continue
        for nxt in edge[cur]:
            if finds[nxt]:
                continue
            stack.append(nxt)
            finds[nxt] = True
            ans = max(ans, A[nxt-1]-A[ini-1])

print(ans)
