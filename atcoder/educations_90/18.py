from math import atan2, cos, degrees, pi, sin, sqrt

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())

ans = []
for _ in range(Q):
    E = int(input())
    t = 2*pi*E/T
    y, z = -L*sin(t)/2, L/2-L*cos(t)/2
    d = sqrt(X**2 + abs(Y-y)**2)
    ans.append(degrees(atan2(z, d)))

print(*ans, sep="\n")
