N = int(input())
A = list(map(int, input().split()))

s = A[0]
for i in range(1, N):
    s ^= A[i]

ans = [s ^ A[i] for i in range(N)]
print(*ans)
