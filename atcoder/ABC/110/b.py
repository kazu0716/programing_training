N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
x.append(X)
y = list(map(int, input().split()))
y.append(Y)
x.sort()
y.sort()
print("No War" if y[0] - x[-1] >= 1 else "War")