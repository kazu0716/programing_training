N, Q = map(int, input().split())
components = [(i, 0) for i in range(N, 0, -1)]
ans = []
for _ in range(Q):
    query = input().split()
    if query[0] == "1":
        C = query[1]
        x, y = components[-1]
        if C == "R":
            x += 1
        elif C == "L":
            x -= 1
        elif C == "U":
            y += 1
        else:
            y -= 1
        components.append((x, y))
    else:
        p = int(query[1])
        ans.append(f"{components[-p][0]} {components[-p][1]}")
print(*ans, sep="\n")
