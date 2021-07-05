H, W = map(int, input().split())
A = [list(map(int, input().split()))for _ in range(H)]
B = [[0]*W for _ in range(H)]

sum_H, sum_W = [0]*H, [0]*W
for i in range(H):
    for j in range(W):
        a = A[i][j]
        sum_H[i] += a
        sum_W[j] += a

for i in range(H):
    for j in range(W):
        B[i][j] = sum_H[i] + sum_W[j] - A[i][j]
    print(*B[i])
