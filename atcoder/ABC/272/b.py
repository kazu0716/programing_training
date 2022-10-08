from itertools import chain

N, M = map(int, input().split())
attended = [[False]*N for _ in range(N)]
for _ in range(M):
    x = list(map(int, input().split()))[1:]
    for x1 in x:
        for x2 in x:
            attended[x1-1][x2-1] = True
print("No" if False in set(chain.from_iterable(attended)) else "Yes")
