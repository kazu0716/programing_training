N = int(input())
for i in range(int(pow(N, 1 / 3) + 10), 0, -1):
    n = pow(i, 3)
    if n > N:
        continue
    if str(n) == str(n)[::-1]:
        exit(print(n))
