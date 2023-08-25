N = int(input())
S = list(input())
Q = int(input())
change = []
is_upper = None
for _ in range(Q):
    t, x, c = input().split()
    if t == "1":
        S[int(x) - 1] = c
        change.append((int(x) - 1, c))
    elif t == "2":
        is_upper, change = False, []
    else:
        is_upper, change = True, []
if is_upper is not None:
    S = [s.upper() for s in S] if is_upper else [s.lower() for s in S]
for i, c in change:
    S[i] = c
print(*S, sep="")
