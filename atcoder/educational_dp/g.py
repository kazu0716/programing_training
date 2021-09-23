from collections import deque

N, M = map(int, input().split())

edge = [[] for _ in range(N)]
in_cnt = [0] * N

for _ in range(M):
    x, y = map(int, input().split())
    edge[x-1].append(y-1)
    in_cnt[y-1] += 1

dp = [0] * N
q = deque([n for n in range(N) if in_cnt[n] == 0])

while q:
    v = q.popleft()
    for nxt in edge[v]:
        if dp[nxt] < dp[v] + 1:
            dp[nxt] = dp[v] + 1
        in_cnt[nxt] -= 1
        if in_cnt[nxt] == 0:
            q.append(nxt)

print(max(dp))
