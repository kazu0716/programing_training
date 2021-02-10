from math import sqrt

n = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))

p1, p2_, p3_ = 0, 0, 0
p_inf_ = []

for i in range(n):
    p1 += abs(X[i] - Y[i])
    p2_ += abs(X[i] - Y[i]) ** 2
    p3_ += abs(X[i] - Y[i]) ** 3
    p_inf_.append(abs(X[i] - Y[i]))

ans = [p1, sqrt(p2_), p3_ ** round((1/3), 32), max(p_inf_)]
print(*ans, sep="\n")
