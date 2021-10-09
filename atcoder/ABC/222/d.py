N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
MOD = 998244353

mi, ma = A[0], B[-1]
diff = ma - mi + 1
dp = [[0]*diff for _ in range(N)]
cnt = [[0]*diff for _ in range(N)]

for i in range(N):
    a, b = A[i]-mi, B[i]-mi
    for j in range(diff):
        if a <= j and j <= b:
            if i == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = cnt[i-1][j]
        if j == 0:
            cnt[i][j] = dp[i][j]
        else:
            cnt[i][j] = (cnt[i][j-1] + dp[i][j]) % MOD

print(sum(dp[-1]) % MOD)
