N, Q = map(int, input().split())
X = tuple(map(int, input().split()))
edge = [set() for _ in range(N)]
for _ in range(N-1):
    A, B = map(int, input().split())
    if A == B:
        continue
    edge[A-1].add(B-1)
    edge[B-1].add(A-1)
part_tree = [[(X[i], i)] for i in range(N)]
finds, stack = [False]*N, [0]
finds[0] = True
while stack:
    cur = stack[-1]
    if not edge[cur]:
        child = stack.pop()
        if stack:
            combined = list(set(part_tree[stack[-1]]+part_tree[child]))
            part_tree[stack[-1]] = sorted(combined, reverse=True)[:20]
        continue
    nxt = edge[cur].pop()
    if finds[nxt]:
        continue
    finds[nxt] = True
    stack.append(nxt)
ans = []
for _ in range(Q):
    V, K = map(int, input().split())
    ans.append(part_tree[V-1][K-1][0])
print(*ans, sep="\n")
