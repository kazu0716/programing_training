N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(M)]
K = int(input())
CD = [tuple(map(int, input().split())) for _ in range(K)]

ans = 0

for i in range(2**K):
    bit = bin(i)[2:].rjust(K, "0")
    t_a, dishes = 0, []
    for j, b in enumerate(tuple(bit)):
        c = CD[j]
        if b == "0":
            dishes.append(c[0])
        else:
            dishes.append(c[1])

    st = set(dishes)

    for ab in AB:
        if ab[0] in st and ab[1] in st:
            t_a += 1

    ans = max(ans, t_a)

print(ans)
