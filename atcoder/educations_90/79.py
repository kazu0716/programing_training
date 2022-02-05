from sys import exit

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]
ans = 0
for h in range(H-1):
    for w in range(W-1):
        if A[h][w] == B[h][w]:
            continue
        ans += abs(A[h][w]-B[h][w])
        for dh, dw in ((1, 0), (0, 1), (1, 1)):
            A[h+dh][w+dw] -= A[h][w]-B[h][w]

for h in range(H):
    if A[h][-1] != B[h][-1]:
        print("No")
        exit()
for w in range(W):
    if A[-1][w] != B[-1][w]:
        print("No")
        exit()

print(*("Yes", ans), sep="\n")
