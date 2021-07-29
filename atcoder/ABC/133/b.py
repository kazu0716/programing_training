N, D = map(int, input().split())
X = []

ans = 0

for _ in range(N):
    X.append(tuple(map(int, input().split())))

for i in range(N):
    for j in range(i, N):
        xi, xj = X[i], X[j]
        d2 = 0
        for k in range(D):
            d2 += (xi[k] - xj[k]) ** 2
        n = 1
        while n * n <= d2:
            if n * n == d2:
                ans += 1
                break
            n += 1

print(ans)
