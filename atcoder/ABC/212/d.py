from heapq import heappop, heappush

Q = int(input())

bag, ans = [], []
cnt = 0

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        heappush(bag, query[1]-cnt)
    elif query[0] == 2:
        cnt += query[1]
    else:
        ans.append(heappop(bag)+cnt)

print(*ans, sep="\n")
