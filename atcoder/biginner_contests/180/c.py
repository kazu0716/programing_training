N = int(input())
ans, n = [], 1

while n*n <= N:
    if N % n == 0:
        ans.append(n)
        if n != N // n:
            ans.append(N//n)
    n += 1

ans.sort()
print(*ans, sep="\n")
