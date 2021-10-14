from heapq import heappop, heappush

N, M = map(int, input().split())
A = []

for a in map(int, input().split()):
    heappush(A, -a)

while M > 0:
    c = heappop(A)
    if c % 2 != 0:
        c = c // 2 + 1
    else:
        c //= 2
    heappush(A, c)
    M -= 1

print(-sum(A))
