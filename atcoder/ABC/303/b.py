N, M = map(int, input().split())
discords = [set([j for j in range(N) if i != j]) for i in range(N)]
ans = 0
for _ in range(M):
    A = list(map(lambda x: int(x) - 1, input().split()))
    for i in range(N):
        if 0 <= i - 1 < N:
            discords[A[i]].discard(A[i - 1])
            discords[A[i - 1]].discard(A[i])
        if 0 <= i + 1 < N:
            discords[A[i]].discard(A[i + 1])
            discords[A[i + 1]].discard(A[i])
for d in discords:
    ans += len(d)
print(ans // 2)
