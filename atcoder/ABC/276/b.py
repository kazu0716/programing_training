N, M = map(int, input().split())
edge = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    edge[A].append(B)
    edge[B].append(A)
for i in range(1, N+1):
    print(len(edge[i]), *sorted(edge[i]))
