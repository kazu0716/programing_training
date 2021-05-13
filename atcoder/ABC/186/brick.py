N, W = map(int, input().split())
ans = 0

while True:
    ans += 1
    if W * ans > N:
        break
print(ans-1)
