N = int(input())
A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))

mi, ma = 0, 10000

for i in range(N):
    a, b = A[i], B[i]
    mi, ma = max(min(a, b), mi), min(max(a, b), ma)

ans = ma-mi+1

if ans > 0:
    print(ans)
else:
    print(0)
