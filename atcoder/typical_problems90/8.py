N = int(input())
S = tuple(input())
atcoder = " atcoder"
mod = pow(10, 9) + 7

dp = [[0] * len(atcoder) for _ in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
    s = S[i-1]
    for j in range(len(atcoder)):
        if s == atcoder[j]:
            dp[i][j] += (dp[i - 1][j - 1] + dp[i - 1][j]) % mod
        else:
            dp[i][j] += dp[i - 1][j] % mod

print(dp[-1][-1])
