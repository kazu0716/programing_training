A, B = map(int, input().split())

ans = 0

for i in range(B, 0, -1):
    if B//i - (A-1)//i >= 2:
        ans = i
        break

print(ans)
