from collections import defaultdict

N = int(input())
S = input()
cnt = defaultdict(int)
i = j = 0
while i < N:
    c = S[i]
    while j < N and S[j] == c:
        j += 1
    cnt[c] = max(cnt[c], j - i)
    i = j
print(sum(cnt.values()))
