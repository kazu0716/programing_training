N = int(input())

edge = [[] for _ in range(N)]
flag = False
for _ in range(N-1):
    a, b = map(int, input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)

for i in range(N):
    n = len(edge[i])
    if n == N-1:
        flag = True

if flag:
    print("Yes")
else:
    print("No")
