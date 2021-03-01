from math import log

P = float(input())

x = 0.0
low = 0.0
high = P

while high - low > pow(10, -8) and P > 1:
    mid = (low + high) / 2
    guess = 1 + log(2**(-1/1.5)) * P * (2 ** (-mid/1.5))

    if abs(guess) < pow(10, -8):
        x = mid
        break
    elif guess <= -pow(10, -8):
        low = mid
        continue
    elif guess >= pow(10, -8):
        high = mid
        continue

if P > 1:
    ans = x + P / 2 ** (x/1.5)
    print(ans)
else:
    print(P)
