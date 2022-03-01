from sys import exit

N = int(input())
S = [list(input()) for _ in range(N)]
p = []
for i in range(N):
    for j in range(N):
        if S[i][j] == "#":
            p.append((i, j))
while p:
    sh, sw = p.pop()
    for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)):
        cur_h, cur_w = sh, sw
        cnt, changed = 1, 0
        for _ in range(5):
            cur_h += dh
            cur_w += dw
            if cur_w < 0 or cur_w >= N or cur_h < 0 or cur_h >= N:
                break
            if S[cur_h][cur_w] == ".":
                changed += 1
                if changed > 2:
                    break
            cnt += 1
        if cnt == 6:
            print("Yes")
            exit()
print("No")
