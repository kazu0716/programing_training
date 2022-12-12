from math import ceil, floor


def get_fall_time(t):
    return A * pow(1 + t, -1/2) + B * t if t > 0 else A


A, B = map(int, input().split())
cnt = pow(A/(2*B), 2/3) - 1
print(min(get_fall_time(ceil(cnt)), get_fall_time(floor(cnt))))
