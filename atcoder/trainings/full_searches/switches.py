N, M = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(M)]
P = list(map(int, input().split()))

ans = 0

for i in range(2 ** N):
    bit = bin(i)[2:].rjust(N, "0")
    flag = True
    for j in range(M):
        cnt = 0
        k = S[j][0]
        for n in range(1, k + 1):
            if bit[S[j][n]-1] == "1":
                cnt += 1
        if cnt % 2 != P[j]:
            flag = False
    if flag:
        ans += 1

print(ans)
