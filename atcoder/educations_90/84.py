from bisect import bisect_right

N = int(input())
S = input()
cnt = [[], []]
for i, s in enumerate(S):
    if s == "o":
        cnt[0].append(i)
    else:
        cnt[1].append(i)
cnt[0].sort()
cnt[1].sort()
ans = 0
for l in range(N):
    is_c = S[l] == "o"
    idx = bisect_right(cnt[is_c], l)
    if idx >= len(cnt[is_c]):
        continue
    ans += N-cnt[is_c][idx]
print(ans)
