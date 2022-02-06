N = int(input())
dp = [[0]*1002 for _ in range(1002)]

for _ in range(N):
    lx, ly, rx, ry = map(int, input().split())
    dp[lx][ly] += 1
    dp[lx][ry] -= 1
    dp[rx][ly] -= 1
    dp[rx][ry] += 1

for x in range(1001):
    for y in range(1001):
        dp[x][y+1] += dp[x][y]
for x in range(1001):
    for y in range(1001):
        dp[x+1][y] += dp[x][y]

ans = [0]*(N+1)
for x in range(1001):
    for y in range(1001):
        ans[dp[x][y]] += 1
print(*ans[1:N+1], sep="\n")
