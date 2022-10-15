X, K = map(int, input().split())
for i in range(K):
    X //= pow(10, i)
    m = X % 10
    X += -m if m <= 4 else 10-m
    X *= pow(10, i)
print(X)
