N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
dp = [[False]*N for _ in range(2)]
dp[0][0], dp[1][0] = True, True
for i in range(1, N):
    Ai, Ai1 = A[i-1], A[i]
    Bi, Bi1 = B[i-1], B[i]
    for j in range(2):
        if j == 0:
            if abs(Ai-Ai1) <= K and dp[0][i-1]:
                dp[0][i] = True
            if abs(Ai-Bi1) <= K and dp[0][i-1]:
                dp[1][i] = True
        else:
            if abs(Bi-Bi1) <= K and dp[1][i-1]:
                dp[1][i] = True
            if abs(Bi-Ai1) <= K and dp[1][i-1]:
                dp[0][i] = True
if dp[0][-1] or dp[1][-1]:
    print("Yes")
else:
    print("No")
