from itertools import permutations

N, M = map(int, input().split())

ans = 0
pathes = [[0] * N for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    pathes[a-1][b-1] = 1
    pathes[b-1][a-1] = 1

for path in permutations(range(N)):
    flag = 1
    if path[0] != 0:
        break
    for n in range(N-1):
        i = path[n]
        j = path[n+1]
        flag *= pathes[i][j]
    if flag == 1:
        ans += 1

print(ans)
