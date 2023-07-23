H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
for i in range(H):
    for j in range(W):
        if S[i][j] == "#" and not ((0 <= i - 1 < H and S[i - 1][j] == "#") or (0 <= i + 1 < H and S[i + 1][j] == "#") or (0 <= j - 1 < W and S[i][j - 1] == "#") or (0 <= j + 1 < W and S[i][j + 1] == "#")):
            exit(print("No"))
print("Yes")
