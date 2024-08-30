N, Q = map(int, input().split())
S = input()
accumlation = [0]
for i in range(1, N):
    accumlation.append(accumlation[-1] + (1 if S[i] == S[i - 1] else 0))
ans = []
for _ in range(Q):
    l, r = map(int, input().split())
    ans.append(accumlation[r - 1] - accumlation[l - 1])
print(*ans, sep="\n")
