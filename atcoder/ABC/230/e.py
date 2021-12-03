N = int(input())

div = [1, N]
i, pre = 2, N
while i*i <= N:
    if N // i != pre:
        div.append(i)
        div.append(N//i)
        pre = N // i
    i += 1
div.sort()

ans = N
for i in range(1, len(div)):
    n1, n2 = div[i-1], div[i]
    ans += (N//n2)*(n2-n1)
print(ans)
