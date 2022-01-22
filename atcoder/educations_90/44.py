from collections import deque

N, Q = map(int, input().split())
A = deque(list(map(int, input().split())))
ans = []
for _ in range(Q):
    T, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    if T == 1:
        x, y = A[X], A[Y]
        A[X], A[Y] = y, x
    elif T == 2:
        p = A.pop()
        A.appendleft(p)
    else:
        ans.append(A[X])

print(*ans, sep="\n")
