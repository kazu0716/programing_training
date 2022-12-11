H, W = map(int, input().split())
S, T = [list(input()) for _ in range(H)], [list(input()) for _ in range(H)]
S_t, T_t = [list(s) for s in zip(*S)], [list(t) for t in zip(*T)]
print("Yes" if sorted(S_t) == sorted(T_t) else "No")
