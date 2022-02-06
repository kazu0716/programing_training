from math import gcd

A, B = map(int, input().split())
lcm = (A*B)//gcd(A, B)
if lcm > pow(10, 18):
    print("Large")
else:
    print(lcm)
