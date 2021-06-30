N = int(input())
flag = False

for i in range(1, 10):
    for j in range(1, 10):
        if i * j != N:
            continue
        flag = True
        break
    else:
        continue
    break

if flag:
    print("Yes")
else:
    print("No")
