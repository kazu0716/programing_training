H = W = 9
A = [list(map(int, input().split())) for _ in range(H)]
target = set(range(1, 10))
for i in range(H):
    if set(A[i]) != target:
        exit(print("No"))
for j in range(W):
    column = set()
    for i in range(H):
        column.add(A[i][j])
    if column != target:
        exit(print("No"))
for i in range(0, H, 3):
    for j in range(0, W, 3):
        square = set()
        for ii in range(i, i + 3):
            for jj in range(j, j + 3):
                square.add(A[ii][jj])
        if square != target:
            exit(print("No"))
print("Yes")
