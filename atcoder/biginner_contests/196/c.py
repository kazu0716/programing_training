N = int(input())
l = len(str(N))

ans = 0

if l >= 2:
    for i in range(1, 10):
        if int(str(i) + str(i)) <= N:
            ans += 1
        else:
            break

if l >= 4:
    for i in range(10, 100):
        if int(str(i) + str(i)) <= N:
            ans += 1
        else:
            break

if l >= 6:
    for i in range(100, 1000):
        if int(str(i) + str(i)) <= N:
            ans += 1
        else:
            break

if l >= 8:
    for i in range(1000, 10000):
        if int(str(i) + str(i)) <= N:
            ans += 1
        else:
            break

if l >= 10:
    for i in range(10000, 100000):
        if int(str(i) + str(i)) <= N:
            ans += 1
        else:
            break

if l >= 12:
    for i in range(100000, 1000000):
        if int(str(i) + str(i)) <= N:
            ans += 1
        else:
            break

print(ans)
