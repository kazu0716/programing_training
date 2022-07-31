Y = int(input())
q = Y % 4
if q == 0:
    print(Y+2)
elif q == 1:
    print(Y+1)
elif q == 2:
    print(Y)
else:
    print(Y+3)
