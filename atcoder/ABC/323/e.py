from collections import defaultdict

N, X = map(int, input().split())
T = list(map(int, input().split()))
MOD = 998244353
first_song = T[0]
T.sort()
inv_mod = pow(N, -1, MOD)
dp = defaultdict(int)
dp[0] = 1
ans = 0
for i in range(X + 1):
    if i not in dp:
        continue
    if i + first_song >= X + 0.5:
        ans = (ans + dp[i] * inv_mod) % MOD
    for t in T:
        if i + t > X:
            break
        dp[i + t] = (dp[i + t] + dp[i] * inv_mod) % MOD
print(ans)
