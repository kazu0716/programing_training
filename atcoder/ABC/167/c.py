N, M, X = map(int, input().split())
CA = [list(map(int, input().split())) for _ in range(N)]

ans = pow(10, 10)

for i in range(1, 2**N):
    bit = bin(i)[2:].rjust(N, "0")
    cost, cap = 0, [0]*M
    for i, b in enumerate(list(bit)):
        if b == "0":
            continue
        cost += CA[i][0]
        for j in range(1, M+1):
            cap[j-1] += CA[i][j]

    flag = True
    for c in cap:
        if c < X:
            flag = False
            break

    if flag:
        ans = min(ans, cost)

if ans == pow(10, 10):
    print(-1)
else:
    print(ans)
