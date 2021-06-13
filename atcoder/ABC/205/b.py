N = int(input())
A = list(map(int, input().split()))

flag = True
A.sort()
for i in range(N):
    if i+1 == A[i]:
        continue
    flag = False
    break

if flag:
    print("Yes")
else:
    print("No")
