N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0
pre_idx = -1

for i in range(N):
    idx = A[i] - 1
    ans += B[idx]
    if pre_idx != -1 and idx - pre_idx == 1:
        ans += C[pre_idx]
    pre_idx = idx

print(ans)
