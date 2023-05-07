A, B, K = map(int, input().split())
if A > B:
    A, B = B, A
for d in range(A, 0, -1):
    if A % d == B % d == 0:
        K -= 1
    if K == 0:
        print(d)
        exit()
