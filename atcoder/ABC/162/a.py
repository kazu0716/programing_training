N = input()
flag = False

for n in N:
    if n == "7":
        flag = True
        break

if flag:
    print("Yes")
else:
    print("No")
