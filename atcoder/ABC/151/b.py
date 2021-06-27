N, K, M = map(int, input().split())
A = list(map(int, input().split()))

ans = -1
for i in range(K+1):
    avg = (sum(A) + i) / N
    if avg >= M:
        ans = i
        break

print(ans)
