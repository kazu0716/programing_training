from bisect import bisect_left, bisect_right

N = int(input())
A = list(input().split())
A.sort()

flag = True

for a in A:
    left, right = bisect_left(A, a), bisect_right(A, a)
    if right - left != 1:
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")
