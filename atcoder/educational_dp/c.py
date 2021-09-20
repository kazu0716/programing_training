N = int(input())

dp = [[0]*3 for _ in range(N+1)]
dp[0] = [0, 0, 0]

for i in range(1, N+1):
    a, b, c = map(int, input().split())
    dp_a, dp_b, dp_c = dp[i-1][0], dp[i-1][1], dp[i-1][2]
    dp[i][0] = max(dp_b+a, dp_c+a)
    dp[i][1] = max(dp_a+b, dp_c+b)
    dp[i][2] = max(dp_a+c, dp_b+c)

print(max(dp[-1]))
