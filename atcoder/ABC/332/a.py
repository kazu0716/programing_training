N, S, K = map(int, input().split())
ans = 0
for _ in range(N):
    P, Q = map(int, input().split())
    ans += P * Q
ans += 0 if ans >= S else K
print(ans)
