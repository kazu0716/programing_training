N = int(input())
A = [0] + list(map(int, input().split()))

dp = [0] * (N+1)
ans = []

for i in range(N, 0, -1):
    cnt = 0
    for j in range(i, N+1, i):
        cnt += dp[j]
    if cnt % 2 != A[i]:
        dp[i] = 1
        ans.append(i)

n = len(ans)
print(n)
if n > 0:
    print(*ans[::-1])
