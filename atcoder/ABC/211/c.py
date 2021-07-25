S = input()
n = len(S)
chokudai = " chokudai"
mod = pow(10, 9) + 7
dp = [[0] * len(chokudai) for _ in range(n+1)]

for i in range(n+1):
    dp[i][0] = 1

for i in range(1, n+1):
    for j in range(1, len(chokudai)):
        if S[i-1] == chokudai[j]:
            dp[i][j] = (dp[i-1][j] + dp[i-1][j-1]) % mod
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][len(chokudai)-1])
