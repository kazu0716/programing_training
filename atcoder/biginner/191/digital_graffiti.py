H, W = map(int, input().split())
L = [list(input()) for _ in range(H)]

ans = 0

for x in range(1, H):
    for y in range(1, W):
        count = 0
        for i in range(2):
            for j in range(2):
                if L[x-i][y-j] == "#":
                    count += 1
        if count % 2 == 1:
            ans += 1
print(ans)
