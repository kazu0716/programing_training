N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

ans = []
for i in range(P, Q+1):
    tmp = []
    for j in range(R, S+1):
        if abs(A-i) == abs(B-j):
            tmp.append("#")
        else:
            tmp.append(".")
    ans.append("".join(tmp))

print(*ans, sep="\n")
