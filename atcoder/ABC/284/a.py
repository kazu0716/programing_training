N = int(input())
print(*[input() for _ in range(N)][::-1], sep="\n")
