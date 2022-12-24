S = list(input())
ans = 0
while S:
    if len(S) >= 2 and S[-1] == S[-2] == "0":
        S.pop()
    S.pop()
    ans += 1
print(ans)
