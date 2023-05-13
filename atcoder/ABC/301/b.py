N = int(input())
A = list(map(int, input().split()))
ans = []
for i in range(N - 1):
    ans.append(A[i])
    if abs(A[i] - A[i + 1]) > 1:
        ans += list(range(A[i] + 1, A[i + 1]) if A[i] < A[i + 1] else range(A[i] - 1, A[i + 1], -1))
ans.append(A[-1])
print(*ans)
