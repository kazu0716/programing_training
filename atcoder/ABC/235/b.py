N = int(input())
H = tuple(map(int, input().split()))

ans = H[0]
for i in range(1, N):
    if ans < H[i]:
        ans = H[i]
    else:
        break

print(ans)
