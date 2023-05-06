N, Q = map(int, input().split())
S = input()
cnt = [0, 0]
for i in range(1, len(S)):
    cnt.append(cnt[-1] + (1 if S[i - 1:i + 1] == "AC" else 0))
ans = []
for _ in range(Q):
    l, r = map(int, input().split())
    ans.append(cnt[r] - cnt[l])
print(*ans, sep="\n")
