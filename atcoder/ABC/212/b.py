X = list(input())

flag = True

if X.count(X[0]) == 4:
    flag = False
else:
    cnt = 0
    for i in range(len(X)-1):
        x1, x2 = int(X[i]), int(X[i+1])
        if x2 - x1 == 1 or (x1 == 9 and x2 == 0):
            cnt += 1
    if cnt == 3:
        flag = False

if flag:
    print("Strong")
else:
    print("Weak")
