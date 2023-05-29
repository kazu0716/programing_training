def is_ans(cx, cy, hh):
    for x, y, h in xyh:
        if h != max(hh - abs(x - cx) - abs(y - cy), 0):
            return False
    return True


N = int(input())
xyh = [tuple(map(int, input().split())) for _ in range(N)]
ans = []
for cx in range(101):
    for cy in range(101):
        h_set = set()
        for x, y, h in xyh:
            if h <= 0:
                continue
            h_set.add(abs(x - cx) + abs(y - cy) + h)
        if len(h_set) == 1:
            ans.append((cx, cy, h_set.pop()))
for cx, cy, H in ans:
    if is_ans(cx, cy, H):
        print(cx, cy, H)
        exit()
