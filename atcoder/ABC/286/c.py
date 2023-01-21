N, A, B = map(int, input().split())
S = input()
ans = pow(10, 18)
for i in range(N):
    cost = A * i
    for j in range(N // 2):
        left = (i + j) % N
        # NOTE: cast over index to real list index in ring by remainder
        # right = (N - 1 + 2 * i - i - j) % N
        right = (N - 1 + i - j) % N
        if S[left] != S[right]:
            cost += B
    ans = min(ans, cost)
print(ans)
