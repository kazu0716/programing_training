N = int(input())
A = tuple(map(int, input().split()))
INF = pow(10, 18)
dp1, dp2 = [[INF]*2 for _ in range(N)], [[INF]*2 for _ in range(N)]
dp1[0][0], dp2[0][1] = A[0], A[-1]

for i in range(1, N):
    dp1[i][0] = min(dp1[i][0], dp1[i-1][0]+A[i], dp1[i-1][1]+A[i])
    dp1[i][1] = min(dp1[i][1], dp1[i-1][0])
    dp2[i][0] = min(dp2[i][0], dp2[i-1][0]+A[i], dp2[i-1][1]+A[i]) if i < N-1 else min(dp2[i][0], dp2[i-1][0], dp2[i-1][1])
    dp2[i][1] = min(dp2[i][1], dp2[i-1][0])
print(min(dp1[-1][0], dp1[-1][1], dp2[-1][0]))
