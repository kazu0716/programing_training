from collections import deque
from sys import stdin

S = stdin.readline().rstrip()
q = deque()
rev = False

for s in S:
    if s == "R":
        rev = not rev
    elif rev:
        if q and q[0] == s:
            q.popleft()
        else:
            q.appendleft(s)
    else:
        if q and q[-1] == s:
            q.pop()
        else:
            q.append(s)

if rev:
    q.reverse()

print(*q, sep="")
