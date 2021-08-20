N, M = map(int, input().split())

ma, mi = pow(10, 6), 0
for _ in range(M):
    L, R = map(int, input().split())
    mi = max(mi, L)
    ma = min(ma, R)

if ma < mi:
    print(0)
else:
    print(ma - mi + 1)
