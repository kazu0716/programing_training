def get_black_set(D):
    black_set = set()
    for i in range(len(D)):
        for j, s in enumerate(D[i]):
            if s == "#":
                black_set.add((i, j))
    return black_set


def trimmed(C, height):
    a, b, c, d = 1000, 0, 1000, 0
    for h in range(height):
        for w, g in enumerate(C[h]):
            if g == "#":
                a, b, c, d = min(a, h), max(b, h), min(c, w), max(d, w)
    return [C[h][c:d + 1] for h in range(height) if a <= h <= b]


Ha, _ = map(int, input().split())
A = [list(input()) for _ in range(Ha)]
trimmed_A = trimmed(A, Ha)
black_set_A = get_black_set(trimmed_A)
Hb, _ = map(int, input().split())
B = [list(input()) for _ in range(Hb)]
trimmed_B = trimmed(B, Hb)
black_set_B = get_black_set(trimmed_B)
Hx, _ = map(int, input().split())
X = [list(input()) for _ in range(Hx)]
trimmed_X = trimmed(X, Hx)
black_set_X = get_black_set(trimmed_X)
for dha in range(len(trimmed_X)):
    for dwa in range(len(trimmed_X[0])):
        moved_A = set([(ha + dha, wa + dwa) for ha, wa in black_set_A])
        for dhb in range(len(trimmed_X)):
            for dwb in range(len(trimmed_X[0])):
                if black_set_X == moved_A | set([(hb + dhb, wb + dwb) for hb, wb in black_set_B]):
                    print("Yes")
                    exit()
print("No")
