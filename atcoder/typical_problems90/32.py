from itertools import permutations

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
INF = pow(10, 12)

relation = [[True]*N for _ in range(N)]
for _ in range(M):
    X, Y = map(int, input().split())
    relation[X-1][Y-1] = False
    relation[Y-1][X-1] = False

ans = INF
for p in permutations(range(N)):
    flag, cnt = True, 0
    for i in range(N):
        if i+1 < N and not relation[p[i]][p[i+1]]:
            flag = False
            break
        cnt += A[p[i]][i]
    if flag:
        ans = min(ans, cnt)

if ans == INF:
    print(-1)
else:
    print(ans)
