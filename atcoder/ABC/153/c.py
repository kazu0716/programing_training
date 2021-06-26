N, K = map(int, input().split())
H = list(map(int, input().split()))

H.sort()

if K >= N:
    print(0)
else:
    for _ in range(K):
        H.pop()
    print(sum(H))
