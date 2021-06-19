N = int(input())
T = list(map(int, input().split()))
s = sum(T)

dp = [[False] * (s + 1) for _ in range(N + 1)]
dp[0][0] = True

for i in range(N):
    for j in range(s + 1):
        if T[i] <= j:
            dp[i + 1][j] = dp[i][j - T[i]] or dp[i][j]
        else:
            dp[i + 1][j] = dp[i][j]

for i in range(s//2, s+1):
    if dp[N][i]:
        print(max(i, s-i))
        break
