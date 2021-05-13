N = int(input())
A = list(map(int, input().split()))

s = 1

if 0 in A:
    s = 0
else:
    for a in A:
        s *= a
        if s > pow(10, 18):
            s = -1
            break

print(s)
