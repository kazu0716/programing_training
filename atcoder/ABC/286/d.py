N, X = map(int, input().split())
coin = [tuple(map(int, input().split())) for _ in range(N)]
amount = [[False] * (X + 1) for _ in range(N + 1)]
amount[0][0] = True
for i in range(N):
    A, B = coin[i]
    for j in range(X + 1):
        if not amount[i][j]:
            continue
        for k in range(B + 1):
            total = j + A * k
            if total > X:
                break
            amount[i + 1][total] = True
    if amount[i + 1][-1]:
        print("Yes")
        exit()
print("No")
