from itertools import permutations

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

a, b, i = 0, 0, 0

for p in list(permutations(range(1, N+1), N)):
    if P == list(p):
        a = i
    if Q == list(p):
        b = i
    i += 1

print(abs(a-b))
