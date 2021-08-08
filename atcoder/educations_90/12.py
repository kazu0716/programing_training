H, W = map(int, input().split())
Q = int(input())

fields = [[False] * H for _ in range(W)]

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        r, c = query[1], query[2]
        fields[r-1][c-1] = True
    else:
        ra, ca, rb, cb = query[1], query[2], query[3], query[4]

print(fields)
