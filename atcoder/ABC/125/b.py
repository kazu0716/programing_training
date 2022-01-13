N = int(input())
V, C = tuple(map(int, input().split())), tuple(map(int, input().split()))
ans = -sum(C)

for i in range(2**N):
    tmp = 0
    for j, b in enumerate(tuple(bin(i)[2:].zfill(N))):
        if b == "1":
            tmp += V[j]-C[j]
    ans = max(ans, tmp)

print(ans)
