from math import cos, radians, sqrt

A, B, H, M = map(int, input().split())


def degree_h():
    deg = 90 - 360*(H/12 + M/(60*12))
    if deg > 0:
        return deg
    else:
        return 360 + deg


def degree_m():
    deg = 90 - 360*M/60
    if deg > 0:
        return deg
    else:
        return 360 + deg


dif_deg = abs(degree_h()-degree_m())
d2 = A**2 + B**2 - 2*A*B*cos(radians(dif_deg))
print(sqrt(d2))
