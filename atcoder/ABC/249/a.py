A, B, C, D, E, F, X = map(int, input().split())
tp, tq = divmod(X, A+C)
ap, aq = divmod(X, D+F)
dt = B * (tp+1) * A if tq >= A else B * tp * A + B * tq
da = E * (ap+1) * D if aq >= D else E * ap * D + E * aq
if dt == da:
    print("Draw")
elif dt > da:
    print("Takahashi")
else:
    print("Aoki")
