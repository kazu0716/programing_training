N = int(input())
A = tuple(map(int, input().split()))

ans = []

w_i = A.index(max(A))
s, e, mid = 0, len(A), (0 + 2**N - 1)//2 + 1
if w_i < mid:
    s = mid
else:
    e = mid

for i in range(s, e):
    ans.append((i+1, A[i]))


while len(ans) > 1:
    dl = []
    for j in range(0, len(ans), 2):
        a, b = ans[j], ans[j+1]
        if a[1] > b[1]:
            dl.append(b)
        else:
            dl.append(a)

    for t in dl:
        ans.remove(t)

print(ans[0][0])
