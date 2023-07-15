N = int(input())
S = input()
dp = [[0] * N for _ in range(2)]
dp[int(S[0])][0] = 1
for i in range(1, N):
    if S[i] == "0":
        dp[0][i] = 1
        dp[1][i] = dp[0][i - 1] + dp[1][i - 1]
    else:
        dp[0][i] = dp[1][i - 1]
        dp[1][i] = dp[0][i - 1] + 1
print(sum(dp[1]))
