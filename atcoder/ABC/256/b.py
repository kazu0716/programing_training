N = int(input())
A = list(map(int, input().split()))
P, field = 0, [0, 0, 0, 0]
for Ai in A:
    field[0] += 1
    for x in range(3, -1, -1):
        if x + Ai >= 4:
            P, field[x] = P+field[x], 0
        else:
            field[x+Ai], field[x] = field[x], 0
print(P)
