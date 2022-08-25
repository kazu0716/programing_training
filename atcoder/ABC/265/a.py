X, Y, N = map(int, input().split())
if 3 * X <= Y:
    print(X*N)
else:
    q, r = divmod(N, 3)
    print(Y * q + X * r)
