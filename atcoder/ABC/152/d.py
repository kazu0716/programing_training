N = int(input())

dp = [[0] * 10 for _ in range(10)]
ans = 0

for i in range(1, N+1):
    s = str(i)
    top, btm = int(s[0]), int(s[-1])
    dp[top][btm] += 1

for i in range(10):
    for j in range(10):
        ans += dp[i][j] * dp[j][i]

print(ans)
