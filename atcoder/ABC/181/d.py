from collections import Counter
from itertools import permutations

S = input()
n = len(S)
flag = False


if n >= 3:
    c = dict(Counter(S))
    for i in range(104, 1000, 8):
        counter = dict(Counter(str(i)))
        for key in counter:
            if key not in c:
                break
            if c[key] < counter[key]:
                break
        else:
            flag = True
            break
else:
    for p in permutations(S):
        if int("".join(p)) % 8 == 0:
            flag = True
            break

if flag:
    print("Yes")
else:
    print("No")
