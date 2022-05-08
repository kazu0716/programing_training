N, X, Y = map(int, input().split())
A = list(map(int, input().split()))


def sliding_window(sub):
    r, cnt, cnt_X, cnt_Y = 0, 0, 0, 0
    for l in range(len(sub)):
        while r < len(sub) and (cnt_X <= 0 or cnt_Y <= 0):
            if sub[r] == X:
                cnt_X += 1
            if sub[r] == Y:
                cnt_Y += 1
            r += 1
        if l <= r and cnt_X > 0 and cnt_Y > 0:
            cnt += len(sub) - r + 1
        if sub[l] == X:
            cnt_X -= 1
        if sub[l] == Y:
            cnt_Y -= 1
    return cnt


cur, ans = 0, 0
while cur < N:
    sub_list = []
    while cur < N and Y <= A[cur] <= X:
        sub_list.append(A[cur])
        cur += 1
    if sub_list:
        ans += sliding_window(sub_list)
    else:
        cur += 1
print(ans)
