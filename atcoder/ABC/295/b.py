R, C = map(int, input().split())
B = [list(input()) for _ in range(R)]
for r1 in range(R):
    for c1 in range(C):
        cur = B[r1][c1]
        if cur == "." or cur == "#":
            continue
        for r2 in range(R):
            for c2 in range(C):
                if r1 == r2 and c1 == c2:
                    continue
                d = abs(r1 - r2) + abs(c1 - c2)
                if int(cur) >= d and B[r2][c2] == "#":
                    B[r2][c2] = "."
        B[r1][c1] = "."
for b in B:
    print(*b, sep="")
