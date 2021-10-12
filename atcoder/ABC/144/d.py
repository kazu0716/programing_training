from math import atan2, degrees

a, b, x = map(int, input().split())

if x <= pow(a, 2)*b/2:
    rad = atan2(b, (2*x)/(a*b))
else:
    rad = atan2(2*(b-x*pow(a, -2)), a)

print(degrees(rad))
