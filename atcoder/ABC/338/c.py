N = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
INF = pow(10, 9)

max_x = min([Q[i] // A[i] if A[i] != 0 else INF for i in range(N)])
ans = 0
for x in range(max_x + 1):
    y = INF
    for i in range(N):
        if B[i] == 0:
            continue
        diff = Q[i] - x * A[i]
        if diff <= 0:
            y = min(y, 0)
        else:
            y = min(y, diff // B[i])
    ans = max(ans, x + y)
print(ans)
