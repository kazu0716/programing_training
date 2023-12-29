A, M, L, R = map(int, input().split())
ans = (R - A) // M + (A - L) // M
print(ans + 1)
