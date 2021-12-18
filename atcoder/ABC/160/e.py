X, Y, _, _, _ = map(int, input().split())
P = sorted(list(map(int, input().split())))
Q = sorted(list(map(int, input().split())))
R = sorted(list(map(int, input().split())))

XY, ans = X+Y, 0
while XY > 0:
    p = P[-1] if P and X > 0 else 0
    q = Q[-1] if Q and Y > 0 else 0
    r = R[-1] if R else 0
    n, key = sorted([(p, "p"), (q, "q"), (r, "r")])[-1]
    ans += n
    XY -= 1
    if key == "p":
        P.pop()
        X -= 1
    elif key == "q":
        Q.pop()
        Y -= 1
    else:
        R.pop()

print(ans)
