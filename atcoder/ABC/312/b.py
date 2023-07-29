def is_takcode(i, j):
    for di in range(4):
        for dj in range(4):
            s1, s2 = S[i + di][j + dj], S[i + 8 - di][j + 8 - dj]
            if di < 3 and dj < 3 and s1 == s2 == "#":
                continue
            if (di == 3 or dj == 3) and s1 == s2 == ".":
                continue
            return False
    return True


N, M = map(int, input().split())
S = [input() for _ in range(N)]
ans = []
for i in range(N - 8):
    for j in range(M - 8):
        if is_takcode(i, j):
            ans.append(f"{i + 1} {j + 1}")
print(*ans, sep="\n")
