H, W = map(int, input().split())
coins = [list(map(int, input().split())) for _ in range(H)]
cnt = 0
commands = []
for i in range(H):
    for j in range(W):
        if coins[i][j] % 2 == 0:
            continue
        if 0 <= j + 1 < W:
            coins[i][j] -= 1
            coins[i][j + 1] += 1
            commands.append(f"{i + 1} {j + 1} {i + 1} {j + 2}")
        elif 0 <= i + 1 < H:
            coins[i][j] -= 1
            coins[i + 1][j] += 1
            commands.append(f"{i + 1} {j + 1} {i + 2} {j + 1}")
        else:
            continue
        cnt += 1
print(cnt)
print(*commands, sep="\n")
