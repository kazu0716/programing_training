from collections import deque

S = deque(input())
strings = ["".join(S)]

for _ in range(len(S)):
    s = S.popleft()
    S.append(s)
    strings.append("".join(S))

strings.sort()
print(strings[0])
print(strings[-1])
