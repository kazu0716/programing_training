N = int(input())

ans = 0

for i in range(0, 60):
    if pow(2, i) <= N:
        ans = i
    else:
        break

print(ans)
