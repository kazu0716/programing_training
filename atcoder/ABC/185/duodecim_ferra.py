L = int(input())
a, b = 1, 1

for i in range(1, 12):
    a *= (L-i)
    b *= i

print(a//b)
