from math import sqrt

N, K = map(int, input().split())
A = set(map(int, input().split()))
P = [tuple(map(int, input().split())) for _ in range(N)]
INF, ans = pow(10, 18), 0
for i in range(N):
    d = INF
    for j in A:
        if i != j-1 and i+1 not in A:
            d = min(d, (P[i][0]-P[j-1][0])**2 + (P[i][1]-P[j-1][1])**2)
    ans = max(ans, (0 if d == INF else d))
print(sqrt(ans))
