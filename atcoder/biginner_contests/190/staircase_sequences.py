from math import sqrt

N = int(input())
ans = 0

for i in range(1, int(sqrt(2*N))+1):
    if (2*N/i - i) % 2 == 1:
        ans += 1

print(ans*2)
