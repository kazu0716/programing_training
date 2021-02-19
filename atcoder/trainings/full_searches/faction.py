from itertools import combinations

N, M = map(int, input().split())
C = [[0] * N for _ in range(N)]

ans = 0

for _ in range(M):
    x, y = map(int, input().split())
    C[x-1][y-1] = C[y-1][x-1] = 1


for i in range(2**N, -1, -1):
    flag = True
    bit = bin(i)[2:].rjust(N, "0")

    for c in combinations([i for i, b in enumerate(bit) if b == "1"], 2):
        idx1, idx2 = c[0], c[1]
        bit1, bit2 = int(bit[idx1]), int(bit[idx2])
        if not(C[idx1][idx2] == bit1 and C[idx2][idx1] == bit2):
            flag = False
            break

    if flag:
        ans = max(ans, bit.count("1"))

print(ans)
