from itertools import permutations

k = int(input())
Q = []


def is_diagonal(p, Q):
    for q in Q:
        if p[q[0]] != q[1]:
            return False
    for i, p1 in enumerate(p):
        p_d = i + p1
        n_d = i - p1
        for j, p2 in enumerate(p):
            if i != j and (j+p2 == p_d or j-p2 == n_d):
                return False
    return True


for _ in range(k):
    x, y = map(int, input().split())
    Q.append((x, y))

for p in permutations(range(8)):
    if is_diagonal(p, Q):
        for p_ in p:
            b = list("........")
            b[p_] = "Q"
            print(*b, sep="")
