N = int(input())
A, B = list(map(int, input().split())), list(map(int, input().split()))

cnt = 0

for i in range(N):
    a1, a2 = A[i], A[i+1]
    b = B[i]
    if a1 + a2 <= b:
        cnt += a1 + a2
        A[i], A[i+1] = 0, 0
    elif a1 <= b:
        A[i], A[i+1] = 0, A[i+1] - (b - a1)
        cnt += b
    else:
        A[i] -= b
        cnt += b

print(cnt)
