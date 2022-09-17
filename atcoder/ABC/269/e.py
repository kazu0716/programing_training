N = int(input())
T = 0
low_x, high_x = 0, N
low_y, high_y = 0, N
cnt = 0
while T != -1:
    if cnt % 2 == 0:
        mid = (low_x+high_x)//2
        print("?", low_x, mid, low_y, high_y)
        T = int(input())
        if T <= N - T:
            high_x = mid
            N = T
        else:
            low_x = mid
            N = max(0, N-T)
    else:
        mid = (low_y+high_y)//2
        print("?", low_x, high_x, low_y, mid)
        T = int(input())
        if T <= N - T:
            high_y = mid
            N = T
        else:
            low_y = mid
            N = max(0, N-T)
    if N == 0:
        print("!", min(low_x, high_x), min(low_y, high_y))
