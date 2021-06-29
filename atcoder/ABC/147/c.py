N = int(input())

people = []
ans = 0

for _ in range(N):
    A = int(input())
    states = {}
    for _ in range(A):
        x, y = map(int, input().split())
        states[x-1] = y
    people.append(states)

for i in range(1, 2**N):
    flag = True
    bits = bin(i)[2:].rjust(N, "0")
    for j in range(N):
        if bits[j] == "0":
            continue
        for k, v in people[j].items():
            if bits[k] == str(v):
                continue
            flag = False
            break
        else:
            continue
        break
    if flag:
        ans = max(ans, bits.count("1"))

print(ans)
