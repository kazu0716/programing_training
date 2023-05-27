X, Y, Z = map(int, input().split())
S = input()
INF = pow(10, 18)
dp = [[INF] * 2 for _ in range(len(S) + 1)]
dp[0][0] = 0
for i, s in enumerate(S):
    dp[i][0], dp[i][1] = min(dp[i][0], dp[i][1] + Z), min(dp[i][1], dp[i][0] + Z)
    dp[i + 1][0] = min(dp[i + 1][0], dp[i][0] + (X if s == "a" else Y))
    dp[i + 1][1] = min(dp[i + 1][1], dp[i][1] + (Y if s == "a" else X))
print(min(dp[-1]))
