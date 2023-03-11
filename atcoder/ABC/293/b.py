N = int(input())
A = list(map(int, input().split()))
called = {i: False for i in range(1, N + 1)}
for i, a in enumerate(A):
    if not called[i + 1]:
        called[a] = True
cnt, ans = 0, []
for k, v in called.items():
    if not v:
        cnt += 1
        ans.append(k)
print(cnt)
print(*sorted(ans))
