N, L = map(int, input().split())
MOD = pow(10, 9)+7
dp = [0]*(N+1)
dp[0] = 1

for i in range(N):
    dp[i+1] = (dp[i+1]+dp[i]) % MOD
    if i+L > N:
        continue
    dp[i+L] = (dp[i+L]+dp[i]) % MOD

print(dp[-1])
