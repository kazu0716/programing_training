A, B = map(int, input().split())
cnt = 1

if B == 1:
    print(0)
else:
    for i in range(1, 21):
        cnt += A * 1 - 1
        if cnt >= B:
            print(i)
            break
