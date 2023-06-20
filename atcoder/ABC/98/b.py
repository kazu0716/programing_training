from collections import Counter

N = int(input())
S = input()
ans = 0
for i in range(1, N):
    ans = max(ans, len(set(Counter(S[:i]).keys() & set(Counter(S[i:]).keys()))))
print(ans)
