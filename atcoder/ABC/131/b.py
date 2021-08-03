N, L = map(int, input().split())

s = N * L + sum(range(1, N+1)) - N
pre, ans = pow(10, 9), 0

for i in range(1, N+1):
    d = abs(L + i - 1)
    if pre >= d:
        ans = s - (L + i - 1)
    pre = d

print(ans)
