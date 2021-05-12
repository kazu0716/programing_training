from copy import deepcopy

H, W, K = map(int, input().split())

C = [[0]*W for _ in range(H)]
ans = 0

for i in range(H):
    c = input()
    for j in range(W):
        C[i][j] = c[j]

for n in range(2 ** (H+W)):
    bit = bin(n)[2:].rjust(H+W, "0")
    h_bit, w_bit = bit[:H], bit[H:]
    field = deepcopy(C)

    for i, b in enumerate(h_bit):
        if b == "1":
            for j in range(W):
                field[i][j] = "Red"
    for j, b in enumerate(w_bit):
        if b == "1":
            for i in range(H):
                field[i][j] = "Red"

    cnt = 0
    for i in range(H):
        for j in range(W):
            if field[i][j] == "#":
                cnt += 1
    if cnt == K:
        ans += 1

print(ans)
