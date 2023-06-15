N = int(input())
ans = []
while abs(N) > 0:
    if N % 2 == 0:
        N //= -2
        ans.append("0")
    else:
        N = -(N // 2)
        ans.append("1")
print(*ans[::-1] if ans else "0", sep="")
