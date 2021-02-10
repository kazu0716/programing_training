from math import sin, cos, radians, sqrt

a, b, C = map(int, input().split())

S = a * b * round(sin(radians(C)), 32)/2

a_ = a * round(sin(radians(C)), 32)
b_ = b - a * round(cos(radians(C)), 32)
c = sqrt(a_ ** 2 + b_ ** 2)
L = a + b + c

h = b * round(sin(radians(C)), 32)

print(S)
print(L)
print(h)
