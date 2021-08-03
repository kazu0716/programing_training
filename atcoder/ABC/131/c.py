from math import gcd

A, B, C, D = map(int, input().split())

cd = (C * D) // gcd(C, D)

s = B - A + 1
cnt_c = B // C - (A - 1) // C
cnt_d = B // D - (A - 1) // D
cnt_c_d = B // cd - (A - 1) // cd

print(s - cnt_c - cnt_d + cnt_c_d)
