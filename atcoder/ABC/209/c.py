N = int(input())
C = list(map(int, input().split()))
C.sort()

ans, cnt = 1, 1

for i in range(N):
    ans *= C[i] - cnt + 1
    ans %= pow(10, 9)+7
    cnt += 1

print(ans)
