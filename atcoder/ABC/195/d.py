from bisect import bisect_left

N, M, Q = map(int, input().split())
WV = [list(map(int, input().split())) for _ in range(N)]
WV.sort(key=lambda x: x[1], reverse=True)
X = list(map(int, input().split()))

for _ in range(Q):
    L, R = map(int, input().split())
    boxes = X[:L-1] + X[R:]
    boxes.sort()
    len_box = len(boxes)
    filled = [False] * len_box
    ans = 0

    for i in range(N):
        w, v = WV[i]
        idx = bisect_left(boxes, w)
        if idx == len_box:
            continue

        for j in range(idx, len_box):
            if not filled[j]:
                filled[j] = True
                ans += v
                break

    print(ans)
