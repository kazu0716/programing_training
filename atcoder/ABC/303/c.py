N, M, H, K = map(int, input().split())
S = input()
items = set([tuple(map(int, input().split())) for _ in range(M)])
cur_x, cur_y = 0, 0
for s in S:
    H -= 1
    if H < 0:
        print("No")
        exit()
    if s == "R":
        cur_x += 1
    elif s == "L":
        cur_x -= 1
    elif s == "U":
        cur_y += 1
    else:
        cur_y -= 1
    if (cur_x, cur_y) in items and H < K:
        H = K
        items.remove((cur_x, cur_y))
print("Yes")
