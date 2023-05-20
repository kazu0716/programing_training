def get_sunuke(i, j, di, dj):
    pos = []
    target = "sunuke"
    for k in range(len(target)):
        if not (0 <= i < H and 0 <= j < W) or S[i][j] != target[k]:
            return None
        pos.append(f"{i + 1} {j + 1}")
        i += di
        j += dj
    return pos


H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
for i in range(H):
    for j in range(W):
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)):
            ans = get_sunuke(i, j, di, dj)
            if ans is not None:
                print(*ans, sep="\n")
                exit()
