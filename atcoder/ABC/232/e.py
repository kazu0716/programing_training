H, W, K = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
MOD = 998244353
dp = [[0]*4 for _ in range(K+1)]

if x1 == x2 and y1 == y2:
    dp[0][0] = 1
elif x1 == x2 and y1 != y2:
    dp[0][1] = 1
elif x1 != x2 and y1 == y2:
    dp[0][2] = 1
else:
    dp[0][3] = 1

for k in range(1, K+1):
    dp[k][0] = (dp[k-1][1]+dp[k-1][2]) % MOD
    dp[k][1] = ((W-1)*dp[k-1][0]+(W-2)*dp[k-1][1]+dp[k-1][3]) % MOD
    dp[k][2] = ((H-1)*dp[k-1][0]+(H-2)*dp[k-1][2]+dp[k-1][3]) % MOD
    dp[k][3] = ((H-1)*dp[k-1][1]+(W-1)*dp[k-1][2]+(W+H-4)*dp[k-1][3]) % MOD

print(dp[K][0])
