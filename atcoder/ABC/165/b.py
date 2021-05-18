X = int(input())

c, i = 100, 0

while c < X:
    i += 1
    c += c//100

print(i)
