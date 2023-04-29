from copy import deepcopy

H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
B = [list(input()) for _ in range(H)]
for s in range(H):
    for t in range(W):
        C = deepcopy(A)
        for j in range(W):
            for i in range(H):
                C[i][j] = A[(s + i) % H][j]
        for i in range(H):
            C[i] = C[i][t:] + C[i][:t]
        if C == B:
            print("Yes")
            exit()
print("No")
