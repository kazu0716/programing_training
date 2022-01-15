from collections import defaultdict

N, Q = map(int, input().split())
A = list(map(int, input().split()))

counter = defaultdict(list)
for i in range(N):
    counter[A[i]].append(i+1)

ans = []
for _ in range(Q):
    x, k = map(int, input().split())
    try:
        ans.append(counter[x][k-1])
    except IndexError:
        ans.append(-1)

print(*ans, sep="\n")
