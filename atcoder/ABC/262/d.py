N = int(input())
A = list(map(int, input().split()))
MOD = 998244353

ans = 0
for i in range(1, N+1):
    dp = [[0] * (N+1) for _ in range(N+1)]
    dp[0][0] = 1
    for a in A:
        for j in range(N, 0, -1):
            for k in range(i):
                dp[j][k] = (dp[j][k] + dp[j-1][(k - a) % i]) % MOD
    ans = (ans + dp[i][0]) % MOD
print(ans)
