from collections import defaultdict
from sys import setrecursionlimit

setrecursionlimit(pow(10, 9))


def dfs(cur, cur_num, path):
    global ans
    nxt = ((cur[0] + di) % N, (cur[1] + dj) % N)
    if nxt not in path:
        nxt_num = cur_num * 10 + A[nxt[0]][nxt[1]]
        if nxt_num < ans // pow(10, (N-len(str(nxt_num)))):
            return
        if nxt_num == limit:
            print(limit)
            exit()
        if len(str(nxt_num)) == N:
            ans = max(ans, nxt_num)
            return
        dfs(nxt, nxt_num, list(path)+[nxt])


N = int(input())
A = [list(map(int, input())) for _ in range(N)]
cnt = defaultdict(set)
for i in range(N):
    for j in range(N):
        cnt[A[i][j]].add((i, j))
limit = ""
for k in sorted(cnt, reverse=True):
    limit += str(k)*len(cnt[k])
    if len(limit) >= N:
        break
limit = int(limit[:N])
ans = 0
for i, j in cnt[max(cnt)]:
    for di, dj in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
        dfs((i, j), A[i][j], [(i, j)])
print(ans)
