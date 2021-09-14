from bisect import bisect_left, bisect_right

N = int(input())
A = list(map(int, input().split()))
A.sort()

ans, ma = 0, max(A)
div = set([])

for i in range(0, N):
    a = A[i]
    if i + 1 != bisect_right(A, a):
        div.add(a)
        continue
    for j in range(2*a, ma+1, a):
        idx = bisect_left(A, j)
        if A[idx] == j:
            div.add(j)
    if a not in div:
        ans += 1

print(ans)
