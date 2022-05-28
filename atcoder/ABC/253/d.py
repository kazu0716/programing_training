from math import gcd


def lcm(x, y):
    return (x * y) // gcd(x, y)


def sum_array(a, d, n):
    return n*(2*a+d*(n-1))//2


N, A, B = map(int, input().split())
sn = N*(N+1)//2
sa, sb = sum_array(A, A, N//A), sum_array(B, B, N//B)
AB = lcm(A, B)
sab = sum_array(AB, AB, N//AB)
print(sn-sa-sb+sab)
