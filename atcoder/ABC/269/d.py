from collections import deque


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


N = int(input())
is_black = [[False]*(2001) for _ in range(2001)]
black = []
for _ in range(N):
    X, Y = map(int, input().split())
    X += 1000
    Y += 1000
    i = 2000*X + Y
    black.append((i, X, Y))
    is_black[X][Y] = True
uf = UnionFind(2001*2001)
deq = deque(sorted(black.copy()))
visited = set(deq[0])
while deq:
    cur_i, cur_x, cur_y = deq.popleft()
    for dx, dy in ((-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1)):
        nxt_x, nxt_y = cur_x + dx, cur_y + dy
        if not(0 <= nxt_x <= 2000) or not(0 <= nxt_y <= 2000):
            continue
        if not is_black[nxt_x][nxt_y]:
            continue
        nxt_i = 2000*nxt_x + nxt_y
        if (nxt_i, nxt_x, nxt_y) in visited:
            continue
        uf.union(cur_i, nxt_i)
ans = set()
for i, _, _ in black:
    ans.add(uf.find(i))
print(len(ans))
