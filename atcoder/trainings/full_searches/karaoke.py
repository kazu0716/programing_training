from itertools import combinations

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
C = combinations(range(M), 2)

ans = 0

for c in C:
    s = 0
    for i in range(N):
        s += max(A[i][c[0]], A[i][c[1]])
    ans = max(ans, s)

print(ans)
