N = int(input())
A = list(map(int, input().split()))

dp = [0]*N
cnt = 0
for i in range(N):
    if i % 2 == 0:
        cnt += A[i]
    else:
        cnt -= A[i]
dp[0] = cnt//2

for i in range(N-1):
    dp[i+1] = A[i] - dp[i]

print(*map(lambda x: x*2, dp))
