from math import sqrt

N = int(input())
X = tuple(map(int, input().split()))

l, l2 = [], []

for x in X:
    l.append(abs(x))
    l2.append(x**2)

print(sum(l))
print(sqrt(sum(l2)))
print(max(l))
