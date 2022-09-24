X, Y, Z = map(int, input().split())
if X*Y < 0 or abs(X) < abs(Y):
    print(abs(X))
else:
    if Y*Z < 0 or abs(Z) < abs(Y):
        print(abs(Z) + abs(X-Z))
    else:
        print(-1)
