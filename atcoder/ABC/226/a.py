X = input().split(".")

if int(X[1][0]) <= 4:
    print(X[0])
else:
    print(int(X[0])+1)
