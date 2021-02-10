def divisors(n):
    i = 1
    table = []
    while i * i <= n:
        if n % i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table


l = list(map(int, input().split()))
d = divisors(l[2])

n = 0
for i in d:
    if i >= l[0] and i <= l[1]:
        n += 1
print(n)
