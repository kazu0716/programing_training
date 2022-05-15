W = int(input())
a, b = W//10000, W//100
ans = [i for i in range(1, min(100, W+1))]
if b == 0:
    print(len(ans))
    print(*ans)
    exit()
ans += [i*100 for i in range(1, min(b+1, 100))]
if a == 0:
    print(len(ans))
    print(*ans)
    exit()
ans += [i*10000 for i in range(1, a+1 if a < 100 else a)]
print(len(ans))
print(*ans)
