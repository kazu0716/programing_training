N = int(input())
A = list(map(int, input().split()))
target = sum(A) // N
cnt1 = cnt2 = 0
for a in A:
    if target - a >= 0:
        cnt1 += target - a
    else:
        cnt2 += a - (target + 1)
print(max(cnt1, cnt2))
