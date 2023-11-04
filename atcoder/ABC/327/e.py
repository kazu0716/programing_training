from math import sqrt

N = int(input())
P = tuple(map(int, input().split()))
INF = pow(10, 18) + 0.1
cur, nxt = [-INF] * (N + 1), [-INF] * (N + 1)
cur[0] = 0.0
for i in range(N):
    for j in range(N + 1):
        if cur[j] == -INF:
            continue
        nxt[j] = max(nxt[j], cur[j])
        nxt[j + 1] = max(nxt[j + 1], 0.9 * cur[j] + P[i])
    cur, nxt = nxt.copy(), [-INF] * (N + 1)
divisor = 1.0
ans = -INF
for k in range(1, N + 1):
    ans = max(ans, cur[k] / divisor - 1200 / sqrt(k))
    divisor *= 0.9
    divisor += 1.0
print(ans)
