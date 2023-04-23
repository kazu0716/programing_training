N, T = map(int, input().split())
C = tuple(map(int, input().split()))
R = tuple(map(int, input().split()))
if T not in C:
    T = C[0]
max_r, ans = -1, 0
for i, (c, r) in enumerate(zip(C, R)):
    if c == T and r > max_r:
        max_r, ans = r, i + 1
print(ans)
