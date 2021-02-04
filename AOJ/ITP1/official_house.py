# -*- coding: utf-8 -*-
n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# NOTE: 右記のように宣言すると参照渡しになり、それぞれの階、部屋への値の代入が行われてしまう
#  a = [[[0]*10]*3]*4
b = [[[0]*10 for i in range(3)] for j in range(4)]

for i in l:
    b[i[0]-1][i[1]-1][i[2]-1] += i[3]

flag = False
for i in b:
    if flag:
        print("####################")
    for j in i:
        print(" " + " ".join(list(map(str, j))))
        flag = True
