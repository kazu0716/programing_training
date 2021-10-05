from collections import deque

S = input()
Q = int(input())

rev = False
ans = deque(S)

for _ in range(Q):
    q = input().split()
    if q[0] == "1":
        rev = not rev
    else:
        _, F, C = q
        if rev:
            F = "2" if F == "1" else "1"
        if F == "1":
            ans.appendleft(C)
        else:
            ans.append(C)

if rev:
    ans = list(ans)[::-1]

print(*ans, sep="")
