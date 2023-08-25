M = int(input())
D = list(map(int, input().split()))
ans = (sum(D) + 1) // 2
for i in range(M):
    if ans <= D[i]:
        break
    ans -= D[i]
print(i + 1, ans)
