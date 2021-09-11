P = list(map(int, input().split()))

ans = []

for i in range(len(P)):
    ans.append(chr(P[i]+96))

print(*ans,sep="")
