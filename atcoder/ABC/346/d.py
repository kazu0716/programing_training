N = int(input())
S = input()
C = tuple(map(int, input().split()))
INF = pow(10, 18)
# NOTE: dp[i = the position of string][j = the number of adjacent component][k = the tail bit]
dp = [[[INF] * 2 for _ in range(2)] for _ in range(N)]
# NOTE: dp initial state
dp[0][0][int(S[0])] = 0
dp[0][0][int(S[0]) ^ 1] = C[0]
for i in range(N - 1):
    dp[i + 1][0][0] = min(
        dp[i + 1][0][0], dp[i][0][1] + (0 if S[i + 1] == "0" else C[i + 1])
    )
    dp[i + 1][0][1] = min(
        dp[i + 1][0][1], dp[i][0][0] + (0 if S[i + 1] == "1" else C[i + 1])
    )
    dp[i + 1][1][0] = min(
        dp[i + 1][1][0],
        min(dp[i][0][0], dp[i][1][1]) + (0 if S[i + 1] == "0" else C[i + 1]),
    )
    dp[i + 1][1][1] = min(
        dp[i + 1][1][1],
        min(dp[i][1][0], dp[i][0][1]) + (0 if S[i + 1] == "1" else C[i + 1]),
    )
print(min(dp[-1][1]))
