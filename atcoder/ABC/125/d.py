N = int(input())

cnt = 0
mi, s = pow(10, 18), 0
for A in map(int, input().split()):
    if A < 0:
        cnt += 1
    mi = min(mi, abs(A))
    s += abs(A)

if cnt % 2 == 0:
    print(s)
else:
    print(s-2*mi)
