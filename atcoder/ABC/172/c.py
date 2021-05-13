from itertools import accumulate

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

s_A, s_B = [0]+list(accumulate(A)), [0]+list(accumulate(B))
j, ans = M, 0

for i in range(N+1):
    a = s_A[i]
    if a > K:
        break
    while s_B[j] > K - a:
        j -= 1

    ans = max(ans, i+j)

print(ans)
