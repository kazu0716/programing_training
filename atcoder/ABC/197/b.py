H, W, X, Y = map(int, input().split())

S = [[0] * W for _ in range(H)]
ans = 0

for i in range(H):
    s = list(input())
    for j, c in enumerate(s):
        if c == "#":
            S[i][j] = 1

for x in range(X-1, -1, -1):
    if S[x][Y-1] == 0:
        ans += 1
    else:
        break

for x in range(X, H):
    if S[x][Y-1] == 0:
        ans += 1
    else:
        break

for y in range(Y-2, -1, -1):
    if S[X-1][y] == 0:
        ans += 1
    else:
        break

for y in range(Y, W):
    if S[X-1][y] == 0:
        ans += 1
    else:
        break


print(ans)
