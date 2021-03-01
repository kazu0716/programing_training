N = int(input())
A, B = tuple(map(int, input().split())), tuple(map(int, input().split()))

ans = 0

for i in range(N):
    ans += A[i]*B[i]

if ans == 0:
    print("Yes")
else:
    print("No")
