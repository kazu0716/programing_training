def func(a, b):
    return (a+b)*(a**2+b**2)


N = int(input())
X = pow(10, 19)
limit = pow(10, 6)

j = limit
for i in range(limit):
    while func(i, j) >= N and i <= j:
        X = min(X, func(i, j))
        j -= 1
print(X)
