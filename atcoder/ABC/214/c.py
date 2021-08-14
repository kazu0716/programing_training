N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

dp = [0] * N
dp[0] = T[0]

for i in range(1, N):
    dp[i] = min(dp[i - 1] + S[i - 1], T[i])

dp[0] = min(dp[0], dp[N - 1] + S[N - 1])

for i in range(1, N):
    dp[i] = min(dp[i - 1] + S[i - 1], T[i])

print(*dp, sep="\n")
