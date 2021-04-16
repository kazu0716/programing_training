from itertools import accumulate

N = int(input())
A = tuple(map(int, input().split()))

ans = 0
s = tuple(accumulate(A))

for i in range(N-1):
    ans += A[i]*(s[N-1]-s[i])

print(ans % (pow(10, 9)+7))
