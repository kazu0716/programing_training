from sys import exit

N = int(input())

if N % 2 != 0:
    print(0)
    exit()

N //= 10
ans = N
cnt = 5
while cnt <= N:
    ans += N // cnt
    cnt *= 5

print(ans)
