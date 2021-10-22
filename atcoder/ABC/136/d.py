S = input()
N = len(S)
MAX = 18

dp = [[0]*N for _ in range(MAX)]

for i in range(N):
    dp[0][i] = i + 1 if S[i] == "R" else i - 1

for i in range(MAX-1):
    for j in range(N):
        dp[i+1][j] = dp[i][dp[i][j]]

ans = [0]*N
for j in range(N):
    ans[dp[MAX - 1][j]] += 1

print(*ans)
