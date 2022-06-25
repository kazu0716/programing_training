from collections import defaultdict

N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

field, pos = [False] * N, defaultdict(int)
for i in range(len(A)):
    Ai = A[i] - 1
    field[Ai] = True
    pos[i] = Ai
for l in L:
    l -= 1
    p = pos[l]
    if p >= len(field) - 1 or field[p+1]:
        continue
    field[p], field[p+1] = False, True
    pos[l] += 1
print(*[i+1 for i in range(len(field)) if field[i]])
