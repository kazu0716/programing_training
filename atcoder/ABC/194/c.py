from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))

Sum_A = list(accumulate(A))
Sum_A2 = []

s = 0
for a in A:
    s += a ** 2
    Sum_A2.append(s)

ans = 0

for i in range(1, N):
    ans += (Sum_A2[N-1] - Sum_A2[i-1]) - 2*A[i-1] * \
        (Sum_A[N-1] - Sum_A[i-1]) + (N-i)*A[i-1]**2

print(ans)
