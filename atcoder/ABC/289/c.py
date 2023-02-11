N, M = map(int, input().split())
S = []
for _ in range(M):
    _ = input()
    S.append(set(map(int, input().split())))
ans = 0
for i in range(2**M):
    bit = bin(i)[2:].rjust(M, "0")
    x = set([k for k in range(1, N + 1)])
    for j, b in enumerate(bit):
        if b == "1":
            for y in S[j]:
                x.discard(y)
    if not x:
        ans += 1
print(ans)
