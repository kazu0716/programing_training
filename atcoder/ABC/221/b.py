S = input()
T = input()

flag = False

if S == T:
    flag = True
else:
    for i in range(1, len(T)):
        t = list(T)
        t[i-1] = T[i]
        t[i] = T[i-1]
        if list(S) == t:
            flag = True
            break

if flag:
    print("Yes")
else:
    print("No")
