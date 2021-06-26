N = int(input())

_range, ans = [], 0

for _ in range(N):
    t, l, r = map(int, input().split())
    if t == 1:
        _range.append(("[]", l, r))
    elif t == 2:
        _range.append(("[)", l, r))
    elif t == 3:
        _range.append(("(]", l, r))
    else:
        _range.append(("()", l, r))

for i in range(N-1):
    for j in range(i+1, N):
        sym1, x1, y1 = _range[i]
        sym2, x2, y2 = _range[j]
        if y1 < x2 or x1 > y2:
            continue
        elif (x1 == y2 and sym1[0]+sym2[1] != "[]") or (x2 == y1 and sym2[0]+sym1[1] != "[]"):
            continue
        ans += 1

print(ans)
