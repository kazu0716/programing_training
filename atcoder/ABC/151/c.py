N, M = map(int, input().split())

result = [False] * N
pena = [0] * N
ac, wa = 0, 0

for _ in range(M):
    p, s = input().split()
    p = int(p)

    if not result[p-1] and s == "WA":
        pena[p-1] += 1

    if not result[p-1] and s == "AC":
        result[p-1] = True
        ac += 1
        wa += pena[p-1]

print(ac, wa)
