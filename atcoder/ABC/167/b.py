A, B, C, K = map(int, input().split())

ans = K

if A+B <= K:
    ans = A - (K-A-B)

print(ans)
