N, K = map(int, input().split())
MOD = pow(10, 9) + 7

ans = 0
dp = [[0]*2 for _ in range(N+2)]
dp[1][0] = 0
dp[1][1] = N

for i in range(2, N+2):
    dp[i][0] = dp[i-1][0] + i-1
    dp[i][1] = dp[i-1][1] + N-(i-1)

for i in range(K, N+2):
    s1, s2 = dp[i]
    ans += s2 - s1 + 1
    ans %= MOD

print(ans)
