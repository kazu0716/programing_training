R, C = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(R)]

ans = 0
range_r, range_c = range(R), range(C)
S_ini = [[0] * C for _ in range_r]


for i in range(2 ** R):
    bit = bin(i)[2:].rjust(R, "0")
    s = 0
    S_copy = S_ini
    for j, b in enumerate(list(bit)):
        if b == "1":
            sj = S[j]
            S_copy[j] = list(map(lambda x: (x+1) % 2, sj))
        else:
            S_copy[j] = S[j]

    for c in range_c:
        cnt = 0
        for r in range_r:
            if S_copy[r][c] == 1:
                cnt += 1
        s += max(cnt, R-cnt)
    ans = max(ans, s)

print(ans)
