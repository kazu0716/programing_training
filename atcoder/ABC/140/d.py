N, K = map(int, input().split())
S = list(input())

line = []
for _ in range(len(S)):
    s = S.pop()
    if not line:
        line.append(s)
    else:
        if line[-1] == s:
            continue
        line.append(s)
line = line[::-1]

for _ in range(K):
    for _ in range(2):
        if len(line) > 1:
            line.pop()

ans = (N-1) - (len(line)-1)
print(ans)
