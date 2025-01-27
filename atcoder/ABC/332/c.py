_, M = map(int, input().split())
S = input()
L = _l = 0
m = 0
m += M
for s in S:
    if s == "0":
        m = M
        _l = L
    elif s == "1":
        if m > 0:
            m -= 1
        elif _l > 0:
            _l -= 1
        else:
            L += 1
    else:
        if _l > 0:
            _l -= 1
        else:
            L += 1
print(L)
