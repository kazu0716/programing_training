from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if x < y:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]


N, M, E = map(int, input().split())
conn = defaultdict(tuple)
for i in range(E):
    U, V = map(int, input().split())
    conn[i] = (U-1, V-1)
Q = int(input())
dis_conn = []
for _ in range(Q):
    X = int(input())
    dis_conn.append(conn[X-1])
    del conn[X-1]
uf = UnionFind(N+M)
for k in conn:
    uf.union(conn[k][0], conn[k][1])
cnt = 0
for i in range(N):
    if uf.find(i) >= N:
        cnt += 1
ans = [cnt]
while len(dis_conn) > 1:
    u, v = dis_conn.pop()
    u_par, v_par = uf.find(u), uf.find(v)
    if u_par >= N and v_par < N:
        cnt += uf.size(v)
    elif u_par < N and v_par >= N:
        cnt += uf.size(u)
    ans.append(cnt)
    uf.union(u, v)
print(*ans[::-1], sep="\n")
