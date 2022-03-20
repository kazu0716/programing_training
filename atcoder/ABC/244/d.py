from itertools import permutations

S = list(input().split())
T = list(input().split())
limit = 10
status = tuple(permutations(("R", "G", "B")))
dp = [[False]*6 for _ in range(limit)]
dp[0][status.index(tuple(S))] = True
for i in range(1, limit):
    for j in range(6):
        if not dp[i-1][j]:
            continue
        cur = list(status[j])
        for x, y in ((0, 1), (1, 2), (0, 2)):
            tmp = ["a", "a", "a"]
            tmp[x] = cur[y]
            tmp[y] = cur[x]
            for z in (0, 1, 2):
                if z != x and z != y:
                    tmp[z] = cur[z]
            dp[i][status.index(tuple(tmp))] = True
target = status.index(tuple(T))
for i in range(limit):
    if dp[i][target]:
        break
if i % 2 == 0:
    print("Yes")
else:
    print("No")
