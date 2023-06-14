N, K = map(int, input().split())
_ = input().split()
if N <= K:
    print(1)
    exit()
print((N - 1 + K - 2) // (K - 1))
