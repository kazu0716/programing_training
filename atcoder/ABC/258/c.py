N, Q = map(int, input().split())
S, pos, ans = input(), 0, []
for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        pos = (pos + x) % N
    else:
        ans.append(S[(x - 1 - pos) % N])
print(*ans, sep="\n")
