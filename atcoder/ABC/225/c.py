N, M = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]

cnt_i, cnt_j = divmod(B[0][0], 7)
flag = True

if cnt_i == 0 and cnt_j == 0:
    flag = False
else:
    if cnt_j == 0:
        cnt_i -= 1
        cnt_j = 7
    for i in range(N):
        for j in range(M):
            if 7*(cnt_i+i) + (cnt_j+j) != B[i][j] or cnt_j+j > 7:
                flag = False
                break

if flag:
    print("Yes")
else:
    print("No")
