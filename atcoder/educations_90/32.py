from itertools import permutations

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
INF = pow(10, 12)

no_conn = [set([]) for _ in range(N)]
for _ in range(M):
    X, Y = map(int, input().split())
    no_conn[X-1].add(Y-1)
    no_conn[Y-1].add(X-1)

ans = INF
for p in permutations(range(N)):
    flag, cnt = True, 0
    for i in range(N):
        if (i-1 >= 0 and p[i-1] in no_conn[p[i]]) or (i+1 < N and p[i+1] in no_conn[p[i]]):
            flag = False
            break
        cnt += A[p[i]][i]
    if flag and cnt > 0:
        ans = min(ans, cnt)

if ans == INF:
    print(-1)
else:
    print(ans)
