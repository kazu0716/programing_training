A, B, C, X, Y = map(int, input().split())
ans = float("INF")

for z in range(0, 2*max(X, Y)+1):
    ans = min(C*2*z + A*max(0, X-z) + B*max(0, Y-z), ans)
print(ans)
