N, K = map(int, input().split())
A = tuple(map(int, input().split()))
MAX = 60

dv = [[0]*N for _ in range(MAX)]

for i in range(MAX):
    for j in range(N):
        if i == 0:
            dv[i][j] = A[j] - 1
        else:
            idx = dv[i-1][j]
            dv[i][j] = dv[i-1][idx]

cur = 0
for i in range(MAX):
    if K >> i & 1:
        cur = dv[i][cur]

print(cur+1)
