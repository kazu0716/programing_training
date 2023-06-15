N = int(input())
for i in range((N + 3) // 4 + 1):
    for j in range((N + 6) // 7 + 1):
        c = 4 * i + 7 * j
        if c == N:
            print("Yes")
            exit()
        if c > N:
            break
print("No")
