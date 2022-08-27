def outer_product(ax, ay, bx, by):
    return ax*by-ay*bx


Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())
Cx, Cy = map(int, input().split())
Dx, Dy = map(int, input().split())

ABx, ABy = Bx-Ax, By-Ay
ADx, ADy = Dx-Ax, Dy-Ay
if outer_product(ABx, ABy, ADx, ADy) <= 0:
    print("No")
    exit()

BCx, BCy = Cx-Bx, Cy-By
BAx, BAy = Ax-Bx, Ay-By
if outer_product(BCx, BCy, BAx, BAy) <= 0:
    print("No")
    exit()

CDx, CDy = Dx-Cx, Dy-Cy
CBx, CBy = Bx-Cx, By-Cy
if outer_product(CDx, CDy, CBx, CBy) <= 0:
    print("No")
    exit()


DCx, DCy = Cx-Dx, Cy-Dy
DAx, DAy = Ax-Dx, Ay-Dy
if outer_product(DAx, DAy, DCx, DCy) <= 0:
    print("No")
    exit()

print("Yes")
