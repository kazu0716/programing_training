A = list(map(int, input().split()))
ans = 0
for i, a in enumerate(A):
    if a == 0:
        continue
    ans += pow(2, i)
print(ans)
