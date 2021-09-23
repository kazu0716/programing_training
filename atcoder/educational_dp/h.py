H, W = map(int, input().split())
MOD = pow(10, 9) + 7
grid = [["#"] * (W+1) for _ in range(H+1)]

for i in range(1, H+1):
    tmp = input()
    for j in range(1, W+1):
        grid[i][j] = tmp[j-1]

dp = [[0]*(W+1) for _ in range(H+1)]

for i in range(1, H+1):
    for j in range(1, W+1):
        if i == 1 and j == 1:
            dp[i][j] = 1
        elif grid[i][j] == "#":
            dp[i][j] = 0
        else:
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD

print(dp[-1][-1])
