from collections import deque
from sys import exit, stdin

S = deque(list(stdin.readline()[:-1]))
front, back = 0, 0
while S and S[-1] == "a":
    S.pop()
    back += 1
if not S:
    print("Yes")
    exit()
while S and S[0] == "a":
    S.popleft()
    front += 1
if front > back:
    print("No")
    exit()
S = list(S)
for i in range(len(S)//2+1):
    if S[i] != S[-(i+1)]:
        print("No")
        exit()
print("Yes")
