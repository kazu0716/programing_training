N = int(input())
MOD = 998244353
A, B = [], []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
dp = [[0, 0] for _ in range(N)]
dp[0] = [1, 1]
for i in range(N - 1):
    if A[i] != A[i + 1]:
        dp[i + 1][0] = (dp[i + 1][0] + dp[i][0]) % MOD
    if B[i] != A[i + 1]:
        dp[i + 1][0] = (dp[i + 1][0] + dp[i][1]) % MOD
    if A[i] != B[i + 1]:
        dp[i + 1][1] = (dp[i + 1][1] + dp[i][0]) % MOD
    if B[i] != B[i + 1]:
        dp[i + 1][1] = (dp[i + 1][1] + dp[i][1]) % MOD
print(sum(dp[-1]) % MOD)
