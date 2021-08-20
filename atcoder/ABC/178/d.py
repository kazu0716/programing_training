S = int(input())
mod = pow(10, 9) + 7

dp = [0] * (S+1)

if S >= 3:
    dp[3] = 1
    for n in range(4, S+1):
        dp[n] = (dp[n-1] + dp[n-3]) % mod

print(dp[S])
