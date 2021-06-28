from itertools import permutations

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

n = 1
a, b = 0, 0

for p in permutations(range(1, N+1)):
    p = list(p)
    if p == P:
        a = n
    if p == Q:
        b = n
    n += 1

print(abs(a-b))
