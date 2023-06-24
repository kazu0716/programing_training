_ = input()
A = list(map(int, input().split()))
cur = 0
ans = [0]
for i, a in enumerate(A):
    if cur == i // 7:
        ans[cur] += a
    else:
        ans.append(a)
        cur += 1
print(*ans)
