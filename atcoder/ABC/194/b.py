N = int(input())
A, B, C = [], [], []

for i in range(N):
    a, b = map(int, input().split())
    A.append((i, a))
    B.append((i, b))
    C.append(a+b)

ans = pow(10, 8)

for a in A:
    for b in B:
        if a[0] != b[0]:
            ans = min(ans, max(a[1], b[1]))

for c in C:
    ans = min(ans, c)

print(ans)
