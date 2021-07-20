N = int(input())
H = list(map(int, input().split()))
flag = True
pre = 0

for i in range(N-1):
    h1, h2 = H[i], H[i+1]
    if h2 - h1 >= 1:
        H[i+1] = h2 - 1
        continue
    elif h2 - h1 == 0:
        continue
    flag = False
    break

if flag:
    print("Yes")
else:
    print("No")
