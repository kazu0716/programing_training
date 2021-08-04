from bisect import bisect_left

N, M = map(int, input().split())
A = [int(input()) for _ in range(M)]
A.sort()

dp = [0] * (N + 1)
mod = 1000000007

if M == 0:
    dp[0], dp[1] = 1, 1
    for i in range(2, N + 1):
        dp[i] = (dp[i-1] + dp[i-2]) % mod
else:
    ini = 0
    for i in range(N + 1):
        idx = bisect_left(A, i)
        if idx == M:
            dp[i] = (dp[i-1] + dp[i-2]) % mod
            continue
        if A[idx] != i and ini < 2:
            dp[i] = 1
            ini += 1
            continue
        elif A[idx] == i:
            dp[i] = 0
            continue
        dp[i] = (dp[i-1] + dp[i-2]) % mod

print(dp[-1])
