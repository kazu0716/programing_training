A = [[0]*3 for _ in range(3)]

for i in range(3):
    for j, v in enumerate(list(map(int, input().split()))):
        A[i][j] = v

N = int(input())

for _ in range(N):
    num = int(input())
    for i, a in enumerate(A):
        if num in a:
            A[i][a.index(num)] = 0

flag = False

for a in A:
    if sum(a) == 0:
        flag = True

v1, v2, v3 = 0, 0, 0
dia1, dia2 = 0, 0
for i in range(3):
    for j in range(3):
        if j == 0:
            v1 += A[i][j]
        if j == 1:
            v2 += A[i][j]
        if j == 2:
            v3 += A[i][j]
        if i - j == 0:
            dia1 += A[i][j]
        if i + j == 2:
            dia2 += A[i][j]

if v1 == 0 or v2 == 0 or v3 == 0 or dia1 == 0 or dia2 == 0:
    flag = True

if flag:
    print("Yes")
else:
    print("No")
