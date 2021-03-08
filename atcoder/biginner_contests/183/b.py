Sx, Sy, Gx, Gy = map(int, input().split())

r = Sy/(Sy+Gy)

if Sx <= Gx:
    print(Sx + abs(Sx-Gx)*r)
else:
    print(Sx - abs(Sx-Gx)*r)
