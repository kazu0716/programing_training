N = int(input())
s_set = set()
ans = "Yes"
for _ in range(N):
    S = input()
    if S[0] in ("H", "D", "C", "S") and S[1] in ("A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K") and S not in s_set:
        s_set.add(S)
        continue
    ans = "No"
print(ans)
