from itertools import permutations

A = list(map(int, input().split()))

flag = False

for a1, a2, a3 in permutations(A):
    if a1-a2 == a2-a3:
        flag = True
        break

if flag:
    print("Yes")
else:
    print("No")
