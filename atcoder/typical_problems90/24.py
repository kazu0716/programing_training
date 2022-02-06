N, K = map(int, input().split())
A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))

cnt = 0
for i in range(N):
    cnt += abs(A[i]-B[i])

if K < cnt or (K-cnt) % 2 == 1:
    print("No")
else:
    print("Yes")
