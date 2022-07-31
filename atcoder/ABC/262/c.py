N = int(input())
A = [-1] + list(map(int, input().split()))
cnt, s = 0, [0]
for i in range(1, len(A)):
    if i == A[i]:
        cnt += 1
    s.append(cnt)
ans = 0
for i in range(1, len(A)):
    if i == A[i]:
        ans += s[-1] - s[i]
    elif i < A[i] and A[A[i]] == i:
        ans += 1
print(ans)
