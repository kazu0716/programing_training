K = int(input())
ans = []
for i in range(ord("A"), min(ord("A") + K, ord("Z") + 1)):
    ans.append(chr(i))
print(*ans, sep="")
