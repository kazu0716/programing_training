from sys import stdin

n, m, l = map(int, stdin.readline().split())
A = [list(map(int, stdin.readline().split())) for _ in range(n)]
B = [list(map(int, stdin.readline().split())) for _ in range(m)]

ans = [[0]*l for _ in range(n)]

for i in range(n):
    for j in range(l):
        s = 0
        for k in range(m):
            s += A[i][k]*B[k][j]
        ans[i][j] = s

for a in ans:
    print(*a)
