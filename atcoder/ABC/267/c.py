N, M = map(int, input().split())
A = list(map(int, input().split()))
s = 0
for i in range(M):
    s += (i+1) * A[i]
ans, part_sum = s, sum(A[1:M])
for i in range(N-M):
    s += M*A[M+i] - A[i] - part_sum
    ans = max(ans, s)
    # NOTE: prefix sum doesn't use in this problem, because array A contains negative numbers
    part_sum += A[M+i] - A[i+1]
print(ans)
