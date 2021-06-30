A, B = map(int, input().split())

d = A - 2 * B
if d < 0:
    print(0)
else:
    print(d)
