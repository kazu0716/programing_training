N = int(input())
A = list(map(int, input().split()))
INF = pow(10, 18)
dis, val = [[INF] * N for _ in range(N)], [[0] * N for _ in range(N)]
for i in range(N):
    S = input()
    for j, s in enumerate(S):
        if s == "Y":
            dis[i][j], val[i][j] = 1, A[j]
for k in range(N):
    for i in range(N):
        for j in range(N):
            if dis[i][k] == INF or dis[k][j] == INF:
                continue
            if dis[i][j] > dis[i][k] + dis[k][j]:
                dis[i][j], val[i][j] = dis[i][k] + dis[k][j], val[i][k] + val[k][j]
            elif dis[i][j] == dis[i][k] + dis[k][j]:
                val[i][j] = max(val[i][j], val[i][k] + val[k][j])
Q = int(input())
for _ in range(Q):
    U, V = map(int, input().split())
    d = dis[U - 1][V - 1]
    if d == INF:
        print("Impossible")
    else:
        print(d, A[U - 1] + val[U - 1][V - 1])
