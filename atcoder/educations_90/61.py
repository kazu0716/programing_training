Q = int(input())

front, back = [], []
ans = []
for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        front.append(x)
    elif t == 2:
        back.append(x)
    else:
        ret = front[-x] if x <= len(front) else back[x-len(front)-1]
        ans.append(ret)
print(*ans, sep="\n")
