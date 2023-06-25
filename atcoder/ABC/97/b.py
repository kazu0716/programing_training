X = int(input())
i = 2
ans = 1
while i ** 2 <= X:
    j = 2
    while pow(i, j) <= X:
        j += 1
    ans = max(ans, pow(i, j - 1))
    i += 1
print(ans)
