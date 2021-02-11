def otoshidama():
    N, Y = map(int, input().split())

    x_range = range(min(int(Y/10000), N) + 1)
    y_range = range(min(int(Y/5000), N) + 1)

    for x in x_range:
        for y in y_range:
            # NOTE: x,y,zの3重ループで検索するとTLEになるため、xを消去し探索する
            if (9*x + 4*y) == (Y/1000 - N) and (N-x-y) >= 0:
                return x, y, N-x-y
    return -1, -1, -1


print(*otoshidama())
