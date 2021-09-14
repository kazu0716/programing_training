from bisect import bisect_left, bisect_right

N = int(input())
A = list(map(int, input().split()))
A.sort()

ans, ma = 0, A[-1]
div = set([])

for i in range(0, N):
    a = A[i]
    if i+1 != bisect_right(A, a):
        div.add(a)
        continue
    if a not in div:
        ans += 1
    for j in range(2*a, ma+1, a):
        if A[bisect_left(A, j)] == j:
            div.add(j)

print(ans)
