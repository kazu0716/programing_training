N, T = map(int, input().split())
INF = pow(10, 6)
ans = INF
for _ in range(N):
    c, t = map(int, input().split())
    if t <= T:
        ans = min(ans, c)
print(ans if ans < INF else "TLE")
