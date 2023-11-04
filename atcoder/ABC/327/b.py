B = int(input())
i = 1
while pow(i, i) <= B:
    if pow(i, i) == B:
        print(i)
        exit()
    i += 1
print(-1)
