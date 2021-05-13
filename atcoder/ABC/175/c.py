X, K, D = map(int, input().split())
X = abs(X)
q, mod = divmod(X, D)
n = K-q
if n < 0:
    print(abs(X-K*D))
else:
    if n % 2 == 0:
        print(abs(mod))
    else:
        print(abs(X-D*(q+1)))
