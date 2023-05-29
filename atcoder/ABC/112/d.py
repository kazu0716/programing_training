N, M = map(int, input().split())
i = 1
divisors = []
while i * i <= M:
    if M % i == 0:
        divisors.append(i)
        divisors.append(M // i)
    i += 1
for g in sorted(divisors, reverse=True):
    if M >= g * N:
        print(g)
        exit()
