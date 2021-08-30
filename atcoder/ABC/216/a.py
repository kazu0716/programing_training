X, Y = input().split(".")

Y = int(Y)

if 0 <= Y and Y <= 2:
    print(X + "-")
elif 3 <= Y and Y <= 6:
    print(X)
else:
    print(X + "+")
