N = int(input())
if N == 1:
    exit(print(0))
num = (0, 2, 4, 6, 8)
ans = []
N -= 1
while N > 0:
    ans.append(num[N % 5])
    N //= 5
print(*ans[::-1], sep="")
