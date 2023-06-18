_ = input()
ans = 0
for A in tuple(map(int, input().split())):
    while A % 2 == 0:
        A //= 2
        ans += 1
print(ans)
