N = int(input())

names = []
flag = False

for _ in range(N):
    S, T = input().split()
    names.append([S, T])

for i in range(N-1):
    for j in range(i+1, N):
        if names[i][0] == names[j][0] and names[i][1] == names[j][1]:
            flag = True
            break

if flag:
    print("Yes")
else:
    print("No")
