from collections import Counter
from sys import exit

N = int(input())
A = list(map(int, input().split()))
cnt = Counter(A)

for c in cnt:
    if cnt[c] != 4:
        print(c)
        exit()
