N = int(input())
_range = range(N + 1)
ans = []
for x in _range:
    for y in _range:
        for z in _range:
            if x + y + z <= N:
                ans.append(f"{x} {y} {z}")
print(*ans, sep="\n")
